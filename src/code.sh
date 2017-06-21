#!/bin/bash

# The following line causes bash to exit at any point if there is any error
# and to output each line as it is executed -- useful for debugging
set -e -x -o pipefail

# download vcfs
dx-download-all-inputs 

echo $email

#call python script, passing the email address to be notified
python send_email.py -e $email
