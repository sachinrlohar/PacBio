#!/usr/local/bin/python3

# import required modules
import sys
import io
import re

#-------------------------------------------------------------------
#       
#       Given: At most 10 DNA strings in FASTA format (of length at 
#       most 1 kbp each). 
#       
#       Return: The ID of the string having the highest GC-content, 
#       followed by the GC-content of that string. 
#       
#	This script take input file as a command line argument.
#	Input file should be in FASTA format.
#	
#       EXPECTED OUTPUT FORMAT:
#                               Rosalind_0808
#                               60.919540
#	
#	Usage: ./compute_GC_content.py rosalind_gc.txt
#-------------------------------------------------------------------

# define empty variables 
seq_list = []
header_list = []

# Open input file
seq_file = io.open(sys.argv[1])

string = ''

# This for loop will iterate through file and join all lines to a string
for line in seq_file:
        line = line.strip()
        string += line

# split the string by >
whole_file = string.split('>')

# remove first empty string character
whole_file = whole_file[1:]

# use regex to get each header and each sequence 
for each in whole_file:
        # get header and append to header list
        header_list = re.findall('Rosalind_[0-9]{4}', each )

        # get sequence and append to seq_list
        seq_list = re.findall('Rosalind_[0-9]{4}(.*)', each)

# I need this list to store all gc percentage 
gc_list = []

# Define function to get a list of gc content of each sequence 
def gcCont (seq):
        # gc_list = []
        for i in seq:
                count = 0

                # loop through each base of each sequence
                # and set condition if base is G or C, count it
                for j in range (0, len(i)):
                        if (i[j] == 'G' or i[j] == 'C'):
                                count += 1

                # append the list 
                gc_list.append(count/len(i) * 100)

# call the function to get the gc content list
gcCont(seq_list)

# sort the list to get higest percentage 
sorted_gc = sorted(gc_list)

# This for loop match the highest gc content of the sequence
# and gets it header index from the header list 

for i in range ( 0 , len ( seq_list ) ):
        seq = seq_list[i]
        count = 0
        for j in range ( 0, len(seq) ):
                if ( seq[j] == 'G' or seq[j] == 'C' ):
                        count += 1
        content = count / len(seq) * 100

        # This condition gets the index of the header of 
        # sequence with highest GC content and print it
        if (content == sorted_gc[-1]):
                print(header_list[i])

# print the highest gc content percentage
print("%.6f" % sorted_gc[-1])

# ----------------------------------- END OF THE CODE --------------

