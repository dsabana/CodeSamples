#!/usr/bin/python

"""
TOP TAG 
*******

We are interested seeing what are the top tags used in posts.

Write a mapreduce program that would output Top 10 tags, ordered by 
the number of questions they appear in.

For an extra challenge you can think about how to get a top 10 list of 
tags, where they are ordered by some weighted score of your choice. If 
you decide to do this, then please submit your solution to the regular 
problem and then also submit this extra challenge problem in separate 
files as described on the instruction page.

Please note that you should only look at tags appearing in questions 
themselves (i.e. nodes with node_type "question"), not on answers or 
comments.

"""

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
   
for row in reader:
    if len(row) == 19 and (row[5].strip('"') == 'question' or row[5].strip('"') == 'answer'):
        
	tags = row[2].strip('"').split()
	
	for item in tags:

	    writer.writerow([item])
    



