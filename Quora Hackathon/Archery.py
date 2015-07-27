"""
ARCHERY
*******

Problem Statement
-----------------
The Quora engineering team went to an archery offsite recently.

At the training corner, there was a target on the ground with a pile of arrows on it. Anna
noticed that some of the arrows form the symbol 'Q' by intersecting the rings of the target.

The target is composed of N concentric circles and there are M arrows lying on it, each 
represented as a line segment.

The i-th circle is centered at the origin (0,0) and has radius Ri. The i-th arrow is a line
segment with endpoints (x1i,y1i) and (x2i,y2i).

Now, Anna wonders if it is possible to write a program to quickly count the number of 'Q's 
formed. A 'Q' is defined as a pair of a circle and an arrow such that the arrow intersects 
the circumference of the circle exactly once.

Constraints
-----------
- For 100 percent of the test data, 1≤N,M≤105

- For 50 percent of the test data, 1≤N,M≤103

- All the Ri are less than 106 and greater than 0

- All the coordinates are less than 106 by absolute value

Input Format
------------
- Line 1: One integer N

- Line 2: N integers, Ri (the radii of the circles)

- Line 3: One integer M

- Line 4...M+3: Line 3+i contains 4 integers: x1i, y1i, x2i, y2i, the coordinates of the 
  endpoints of the i-th arrow.

Output Format
-------------
- Line 1: One integer, the number of 'Q's.


Sample Input
------------
4
1 2 3 4
3
1 -1 4 -3
2 1 1 2
1 -2 3 -4

Sample Output
-------------
5

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def binary_search(seq, t):
    min = 0
    max = len(seq) - 1
    while True:
        if max < min:
            return -1
        m = (min + max) // 2
        if (seq[m]*seq[m] >= t and seq[m-1]*seq[m-1] <= t) or (seq[m]*seq[m] >= t and m==0):
            return m
        elif seq[m]*seq[m] < t:
            min = m + 1
        elif seq[m]*seq[m] > t:
            max = m - 1
        
        
n = long(raw_input())
r = sorted(map(lambda x:long(x),raw_input().strip().split()))
r.append(sys.maxint)
m = long(raw_input())
coor = []
for i in range(0,m):
    coor.append(map(lambda x:long(x),raw_input().strip().split()))

count = 0
radii = []
for i in range(0,m):
    x1 = coor[i][0]
    y1 = coor[i][1]
    x2 = coor[i][2]
    y2 = coor[i][3]
    
    radii.append(sorted([x1*x1+y1*y1,x2*x2+y2*y2]))
    
for i in range(0,m):
    ind1 = binary_search(r, radii[i][0])
    ind2 = binary_search(r, radii[i][1])
    count += ind2-ind1

print count