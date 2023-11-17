## The peptide statistics data comes as a un-structured text file.
## We need to structure it in dataframe with spefic features to do analysis and fit models.
## this script will take care of that


## libraries
import re
import glob
import numpy as np
import pandas as pd

## get all the file names in a list
path = r'C:\Users\Swata\Documents\oxidoreductase' # use your path
file_list = glob.glob(path + "/*out.txt")

## get all the separate 500 seq out files and combine all of their containts into one file
with open('oxidoreductase_all.txt', 'w') as merged_file:
    for file_name in file_list:
        # Open each file in the list and read its content
        with open(file_name, 'r') as file:
            content = file.read()
            # Write the content to the merged file
            merged_file.write(content)
            # Add a new line if needed between file contents
            merged_file.write('\n')  # Add a new line after each file's contente"



## read the files and load data
filename = r"C:\Users\Swata\Downloads\oxidoreductase_all.txt"
with open(filename, 'r') as f:
    data = f.read()

## separate each proteins with the help of "PEPSTAT" word in the file
Data = data.split("PEPSTAT")
Data = Data[1:] # remove the first empty element
#print(Data[1:5]) # fair warning lots of lines will be printed 


## get all the numeric values from the unstructured data and separate them into each features
Features = {} # empty dictionary to store all the features

## loop through each protein and get the features
for protein in Data:
    prot = protein.split('\n') # splitting to get each lines
    for line_num in range(len(prot)):
        words = re.split('\t| ',prot[line_num]) # get the words in the lines, including numbers
        
        ## this loop with find the numeric values from the data and bin them with a numeric id for each features
        for id,word in enumerate(words): 
            try:
                 Features[id] = float(word) # all numbers per line will be added
            except:
                pass

#print(Features)

## convert the features dictionary to dataframe
df = pd.DataFrame.from_dict(Features, orient='index')

## save the dataframe to csv
df.to_csv(r"C:\Users\Swata\Final_data\oxidoreductase_structured.csv")