#!/usr/local/bin/python3

# import required modules
import io
import sys


#-------------------------------------------------------------------
#
#	Given: A DNA string of length at most 1 kbp in FASTA format.
#
#	Return: The position and length of every reverse palindrome 
#	in the string having length between 4 and 12. You may return 
#	these pairs in any order.
#
#	This script takes input file from CLI and input file should 
#	in FATSA format.
#
#	EXPECTED OUTPUT FORMAT:
#
#				4 6
#				5 4
#				6 6
#				7 4
#	
#	Usage: ./locate_restriction_site.py rosalind_revp.txt
#-------------------------------------------------------------------


DNA = ""

seq_file = io.open(sys.argv[1])

# Loop through the file to get sequence and join each fragment
for line in seq_file:
	if not '>' in line:
		line = line.rstrip()
		DNA += line


# Define function to get reverse complement of DNA
def rev_comp(dna):
        # Define dictionary for each RV nucleotide
        comp_letter = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        # set empty string
        revCompString = ''
        # for loop for each letter in DNA
        for letter in dna:
                # This will compliment the letter and reverse the string
                # putting comp_letter[letter] bofore revCompString would 
                # reverse the string
                revCompString = comp_letter[letter] + revCompString
        return revCompString

# I need to define res_site function in such a way that it will take kmer 
# of length 4 to 12 nucleotides and reverse complement it and if it is 
# paliandrome then store its count and its position in an array

def res_site(dna):
	# I need empty list to store restriction site
	res_site_list = []
	
	# loop through each number from 4 to 12 
	# to get restriction site of this length

	for i in range (4, 13):
	
		# len(dna) - i + 1 are the number of 
		# iterations I need for each kmer of length i
		
		# A sliding window size between 4 and 12.

		for j in range(1, len(dna) - i + 1):
			
			# condition to check for reverse complement
			if (rev_comp(dna[j:j + i]) == dna[j:j + i] ):
				# if found append its position and length 
				# to the res_site_list
				res_site_list.append(str(j+1) + ' ' + str(i))
	return res_site_list


# to ptint each site on the new line 
# I need to iterate through the function

for site in res_site(DNA):
	print(site)


# ------------------------- END OF THE CODE -------------------------------------
