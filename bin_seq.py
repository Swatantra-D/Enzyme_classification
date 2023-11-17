
## .py version of bin_seq.ipynb. This is easy to run from the terminal and get all the data
# This script will bin the sequences into 500 sequences per file and save them in a folder


##libraries to import
import os

## load the file
filename = r"X:\Data\Sequence_Class\CD-HITTED\4\1650475848.fas.1" # must be a fasta sequence file
with open(filename,'r') as f: #open the file
    data = f.read() # read the file
    f.close # close the file

## 
data_split = data.split('>') # split the file on the basis of the fasta header
data_split = data_split[1:] # remove the first element which is empty
data_split = [">" + seq for seq in data_split] # add the fasta header back to the sequences
identi = [] # list to keep the protein identifiers
sequence = [] # list to keep the sequences


## loop over the data_split and gather the sequences and identifiers
for seq in data_split:
    something = seq.split('\n',1) 
    if len(something) == 1: # if there is no sequence
        pass
    else:
         identi.append(something[0]) # list the identifier
         sequence.append(something[1]) # list the sequence

sequence = [seq.replace('\n','') for seq in sequence] # remove the new line characters from the sequences


## check if all the sequences and identifiers are there
print("got all the values? ", len(identi) == len(sequence))
print("\nlength of the seqences: ", len(sequence))


## Now we'll bin 500 seqences in each files 
for i in range(500,len(identi),500): #
    ofile = open(r"X:\Data\Pepstats\4\binned"+str(i)+'.txt', "w")
    for line in range(i-500,i):
        ofile.write( identi[line] + "\n" + sequence[line] + "\n")
    ofile.close()

## write the remaining sequences in the last file
file = r'X:\Data\Pepstats\4\binned' + str(len(identi))
with open(file,'w') as f:
    for line in range(len(identi)%500):
        f.write(identi[len(identi)%500 - line] + "\n" + sequence[len(identi)%500 - line] + "\n")
        len(identi)%500