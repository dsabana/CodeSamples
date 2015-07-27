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

# MAPPER
# ******
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
   
for row in reader:
    if len(row) == 19:
	id_num, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = row        
	if node_type == 'question':
            writer.writerow([id_num, 'A', node_type, abs_parent_id, len(body)])
        elif row[5] == 'answer':
            writer.writerow([abs_parent_id, 'B', node_type, id_num, len(body)])
  



