## The peptide statistics data comes as a un-structured text file.
## We need to structure it in dataframe with spefic features to do analysis and fit models.

## libraries
import re
import numpy as np
import pandas as pd


## read the files 
filename = r"C:\Users\Swata\Downloads\out.txt"
with open(filename, 'r') as f:
    data = f.read()

## remove the "PEPSTAT" word
Data = data.split("PEPSTAT")
Data = Data[1:]
#print(Data[1:5]) # fair warning lots of lines will be printed 

##
Lines = {i:[] for i in range(49)} # Get all the lines per seqeunce and add line numbers

## get all the numeric values from the unstructured data
for protein in Data:
    prot = protein.split('\n')
    for line_num in range(len(prot)): # get each lines
        words = re.split('\t| ',prot[line_num]) # get the words in the lines including numbers
        for word in words: # this loop with find the numeric values from the data and bin them
            try:
                Lines[line_num].append(float(word)) # all numbers per line will be added
            except:
                pass

#print(Lines)


            