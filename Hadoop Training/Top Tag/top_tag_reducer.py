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

CountTotal = 0
oldTag = None

finalTags = ['fakeTag']
finalCount = [0]
topWhat = 10

for line in sys.stdin:
    thisTag = line.strip()
    
    if oldTag and oldTag != thisTag:
	i = 0	
	for item in finalCount:
	    if CountTotal < item:
		i += 1
	
	if len(finalTags) < topWhat:
	    finalTags.insert(i, oldTag)
	    finalCount.insert(i, CountTotal)
	else:
	    finalTags.insert(i, oldTag)
	    finalCount.insert(i, CountTotal)
	    del finalTags[-1]
	    del finalCount[-1]


        oldTag = thisTag;
        CountTotal = 0

    oldTag = thisTag
    CountTotal += 1

if oldTag != None:
    i = 0	
    for item in finalCount:
        if CountTotal < item:
    	    i += 1
	
    if len(finalTags) < topWhat:
        finalTags.insert(i, oldTag)
	finalCount.insert(i, CountTotal)
    else:
	finalTags.insert(i, oldTag)
	finalCount.insert(i, CountTotal)
	del finalTags[-1]
	del finalCount[-1]


j = 0

print "Tags", "\t", "Count"
while j < topWhat:
    print finalTags[j].strip('"'), "\t", finalCount[j]
    j += 1  







