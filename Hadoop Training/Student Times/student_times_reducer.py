#!/usr/bin/python

"""
STUDENTS AND POSTING TIME ON FORUMS 
***********************************

We have a lot of passionate students that bring a lot of value to forums. 
Forums also sometimes need a watchful eye on them, to make sure that posts
are tagged in a way that helps to find them, that the tone on forums stays 
positive, and in general - they need people who can perform some management 
tasks - forum moderators. These are usually chosen from students who already 
have shown that they are active and helpful forum participants.

Our students come from all around the world, so we need to know both at what 
times of day the activity is the highest, and to know which of the students 
are active at that time.

In this exercise your task is to find for each student what is the hour 
during which the student has posted the most posts. Output from reducers 
should be:

author_id    hour

For example:

13431511\t13
54525254141\t21

If there is a tie: there are multiple hours during which a student has posted 
a maximum number of posts, please print the student-hour pairs on separate lines. 
The order in which these lines appear in your output does not matter.

You can ignore the time-zone offset for all times - for example in the following 
line: "2012-02-25 08:11:01.623548+00" - you can ignore the +00 offset.

In order to find the hour posted, please use the date_added field and NOT the 
last_activity_at field.

"""

import sys

TimeCount = 0
oldID = None
oldTime = None
storedCount = [0]
storedOldTime = [0]

print "Student ID", "\t", "Hour"
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisID, thisTime = data_mapped

    if oldID and oldID != thisID:
	maxCount = max(storedCount)
	maxCountTime = storedOldTime[storedCount.index(maxCount)]
	indices = [i for i, x in enumerate(storedCount) if x == max(storedCount)]
	for j in indices:    
	    print oldID.strip('"'), "\t", storedOldTime[j].strip('"')
		    
        oldID = thisID;
	oldTime = thisTime;
        TimeCount = 0
	storedCount = [0]
	storedOldTime = [0]

    if oldTime and oldTime != thisTime:

	oldTime = thisTime;
        TimeCount = 0

    oldID = thisID
    oldTime = thisTime
    TimeCount += float(1)
    storedCount.append(TimeCount)
    storedOldTime.append(oldTime)

if oldID != None:
    maxCount = max(storedCount)
    maxCountTime = storedOldTime[storedCount.index(maxCount)]
    indices = [i for i, x in enumerate(storedCount) if x == max(storedCount)]
    for j in indices:    
        print oldID.strip('"'), "\t", storedOldTime[j].strip('"')



