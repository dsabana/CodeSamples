
#!/usr/bin/python

"""
POST AND ANSWER LENGTH
**********************

We are interested to see if there is a correlation between the length of a post and 
the length of answers.

Write a mapreduce program that would process the forum_node data and output the length 
of the post and the average answer (just answer, not comment) length for each post. 
You will have to decide how to write both the mapper and the reducer to get the required
result.
"""

# REDUCER
# *******
import sys

OldID_num = None
lenTot = 0
count = 0
lastLetter = None

print "Question Node ID | Question Length | Average Answer Length"

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    
    id_num0, letter, node_type, id_num1, length = data_mapped
   
    if  letter.strip('"') == 'A':
	if lastLetter == 'A':
	    print OldID_num, '\t', oldlength, '\t', old_avg_ans_value
	
	if count > 0:
	    old_avg_ans_value = float(lenTot)/float(count)
	    print OldID_num, '\t', oldlength, '\t', old_avg_ans_value

	OldID_num = id_num0
	oldlength = length
	old_avg_ans_value = 0
	lastLetter = letter.strip('"')
	lenTot = 0
	count = 0
    elif letter.strip('"') == 'B' and id_num0 == OldID_num:
	lenTot += float(length.strip('"'))
	count += float(1)
	lastLetter = letter.strip('"')
	
if  letter.strip('"') == 'A':
    if lastLetter == 'A':
	print OldID_num, '\t', oldlength, '\t', old_avg_ans_value

    if count > 0:
	old_avg_ans_value = float(lenTot)/float(count)
	print OldID_num, '\t', oldlength, '\t', old_avg_ans_value






