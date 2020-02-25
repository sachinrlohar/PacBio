# PacBio


This repository contains two input files, rosalind_gc.fasta and rosalind_revp.txt
for two programms, compute_GC_content.py and locate_restriction_site.py respectively.

Both programms accepts command line arguments.

------------------------------------------------------------------------

Program 1: compute_GC_content.py

This problem is taken from http://rosalind.info/problems/gc/

This program takes fasta input file with multiple sequences and computes it GC content
of each sequence and print header of highest GC content sequence and its GC content in percent.

A pseudo code for GC computation:

                Read File line by line

                        |
                        V

                Store header and sequence
                a seperate lists

                        |
                        V

                Loop through each sequence
                and calculate its GC content
                Define function for computation

                        |
                        V

                Find highest gc content sequence
                and its index number and it is
                the same index number for its header
                in the header list

                        |
                        V

                Print out the output in the
                required format




------------------------------------------------------------------------

program 2: locate_restriction_site.py

This problem is taken from http://rosalind.info/problems/revp/

This file takes input FASTA or txt file with a single sequence and finds
the position and length of every reverse palindrome in the string having
length between 4 and 12.


A pseudo code for locating restriciton site program:

                Read input file line by line and
                store sequence in one single string

                        |
                        V

                Define function to reverse complement
                DNA string with any length

                        |
                        V

                Define function to find palindrome
                restriction site. A sliding window
                size is from 4 to 12. Store found site
                in a list

                        |
                        V

                Loop through this list to print each
                paliandrome restriction site starting
                index and site's length.


------------------------------------------------------------------------
