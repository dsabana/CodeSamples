#!/usr/bin/python

"""
STUDY GROUPS 
************

We might want to help students form study groups. But first we want to see 
if there are already students on forums that communicate a lot between 
themselves.

As the first step for this analysis we have been tasked with writing a 
mapreduce program that for each forum thread (that is a question node with 
all it's answers and comments) would give us a list of students that have 
posted there - either asked the question, answered a question or added a 
comment. If a student posted to that thread several times, they should be 
added to that list several times as well, to indicate intensity of 
communication.

"""

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
   
for row in reader:
    if len(row) == 19:
	id_num, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = row        
	if node_type == 'question':
            writer.writerow([id_num, 'A', author_id])
        elif row[5] == 'answer' or row[5] == 'comment':
            writer.writerow([abs_parent_id, 'B', author_id])
  



