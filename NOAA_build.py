# Creates a main file for historical US NOAA data

# Importing required modules

import pandas as pd
import glob

# Filepath

direc = 'F:/NOAA/raw_data/'

# Build df

for i in range(1929,2022):
    
    files = glob.glob(direc + str(i) + '/*')
    df = pd.DataFrame()
    
    for file in files:
        
        print(file)
        tmp = pd.read_csv(file)
        
        try:
            
            if tmp.NAME[0][-3:] == ' US':
                
                df = pd.concat([df, tmp], axis = 0)
                
            else:
                
                continue
                
        except:
            
            continue
    
    df.to_csv(direc[:8] + 'us_data/NOAA_' + str(i) + '.csv', index = False)

