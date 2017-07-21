# dnanexus_check_for_empty_vcf - v1.0

## What does this app do?
This app takes an array of VCF files produced by the varscan variant caller run during the Amplivar cancer pipeline.

Empty vcfs will be rejected when importing into Ingenuity. 

This app counts the number of variants present in each VCF. A count of empty VCFs is sent via email to the specified email accounts, explaining the absence of any vcfs from Ingenuity.


## What data are required for this app to run?
This app requires two inputs:

1.  A array of vcf files
2. Email addresses - maximum 2 (optional)


## What does this app do?
* This app loops through all the vcf files, selecting the desired vcf file (varscan.vcf - not varscan.bedfiltered.vcf) 
* If there are no variants in the file , add this to a list of 'empty' vcfs
* Once all files have been read an email is sent to the moka-guys mailing list and, if provided, to the email(s) stated in the input.
* If there are 0 empty VCFs an email is still sent confirming that this check has been performed.


## Created by
This app was created within the Viapath Genome Informatics section

