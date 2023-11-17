## This script is used to automatically get the data from emboss pepstat web server
# You'll require the emboss_pepstats.py on path to successfully get the data
# This script will loop over all your sequence files containint 500 sequences(limit for the emboss pepstats server) and get the peptide statistics results

import os # import os module for directory listing and running commands
dir_list = os.listdir() # list all the 500 seq files in the current directory
t_dir = [] # keep a list of files which had a problem running
for dir in dir_list: # loop over all the files
    try:
        command = r'python ./emboss_pepstats.py --email youremail@domain.com --sequence' + dir # 
        os.system(command)
    except:
        t_dir.append(dir)
        continue
print(t_dir) # print the list of files which faced trouble