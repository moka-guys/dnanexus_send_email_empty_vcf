from  email_settings import *
from email.Message import Message
import sys
import getopt
import os
import smtplib

class send_email():
	def __init__(self):
		# email message
		self.email_subject="SWIFT ALERT: Empty VCFs present in run"
		self.email_message=""
		self.email_priority=3
		#list of empty vcfs
		self.list_of_empty_vcfs=[]

	def go(self,argv):
		# capture arguments from command line
		try:
			opts, args = getopt.getopt(argv, 'e:f:')
		except getopt.GetoptError:
			print "Unrecognised flag provided"
			sys.exit()
		
		# capture the email address from the -e and -f arguments
		for opt, arg in opts:
			if opt in('-e','-f'):
				if arg !="ignore":
					#append the email address to the 'you' list (who to send the email to)
					you.append(arg)
		
		# loop through the vcf inouts
		for dir,subdir,filelist in os.walk("/home/dnanexus/in/vcfs/"):
			#for each file
			for file in filelist:
				#set a count for the number fo variants
				variant_count=0
				# print file name
				print file
				# if it's the required vcf # may need changing to bedfiltered.vcf
				if file.endswith('varscan.vcf'):
					#open the file
					with open(os.path.join(dir,file),'r') as vcf:
						# loop through each line
						for line in vcf.readlines():
							#skip headers
							if line.startswith('#'):
								pass
							#count the number of non-empty rows
							elif len(line) >1:
								variant_count+=1
							else:
								pass
				# print the number of variants found
				print "variant count = " + str(variant_count)

				# if it's an empty vcf add to the list
				if variant_count == 0:
					self.list_of_empty_vcfs.append(file)
				else:
					pass


		#if there are empty vcfs 
		if len(self.list_of_empty_vcfs) > 0:
			print "sending email..."
			# set the email message to report a list of empty vcfs, one per line
			self.email_message="The following samples have empty vcfs:\n"+"\n".join(self.list_of_empty_vcfs)
			#send the email
			self.send_an_email()

	def send_an_email(self):
		'''function to send an email. uses self.email_subject, self.email_message and self.email_priority'''	   
		#create message object
		m = Message()
		#set priority
		m['X-Priority'] = str(self.email_priority)
		#set subject
		m['Subject'] = self.email_subject
		#set body
		m.set_payload(self.email_message)
		
		# server details
		server = smtplib.SMTP(host = host,port = port,timeout = 10)
		server.set_debuglevel(1) # verbosity
		server.starttls()
		server.ehlo()
		server.login(user,pw)
		server.sendmail(me, you, m.as_string())

if __name__ == '__main__':
	# Create instance of get_list_of_runs
	email = send_email()
	# call function
	email.go(sys.argv[1:])
