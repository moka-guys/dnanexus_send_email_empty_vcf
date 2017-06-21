# dnanexus_send_email_empty_vcf - v1.0

## What does this app do?
This app takes the output of the varscan variant caller run during the Amplivar cancer pipeline.

This app takes an array of vcf files and sends an email containing any vcfs which do not contain any variants. 

Empty vcfs will be rejected when importing into Ingenuity. 

This email therefore explains the absence of any vcfs from Ingenuity.

## What data are required for this app to run?
This app requires two inputs:

1.  A array of vcf files
2. Email addresses - maximum 2 (optional)


## What does this app do?
* This app loops through all the vcf files, selecting the desired vcf file (varscan.vcf - not varscan.bedfiltered.vcf) 
* If there are no variants in the file , add this to a list of 'empty' vcfs
* Once all files have been read an email is sent to the moka-guys mailing list and, if provided, to the email(s) stated in the input.


## Created by
This app was created within the Viapath Genome Informatics section

