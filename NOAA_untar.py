# This script unzips the NOAA tar files

# Importing required modules

import glob
import tarfile

# NOAA directory

path = 'F:/NOAA/'

# Get list of files to extract

files = glob.glob(path + 'tar/*')

# Main loop

for file in files:
    
    print('Extracting NOAA data from ' + str(file[12:16]) + '.......')
    tar = tarfile.open(file)
    tar.extractall(path + 'raw_data/' + str(file[12:16]))
    tar.close()

