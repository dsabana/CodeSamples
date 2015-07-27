"""
UPVOTES
*******

Problem Statement
-----------------
At Quora, we have aggregate graphs that track the number of upvotes we get each day.

As we looked at patterns across windows of certain sizes, we thought about ways to track 
trends such as non-decreasing and non-increasing subranges as efficiently as possible.

For this problem, you are given N days of upvote count data, and a fixed window size K.
For each window of K days, from left to right, find the number of non-decreasing subranges
within the window minus the number of non-increasing subranges within the window.

A window of days is defined as contiguous range of days. Thus, there are exactly N−K+1 
windows where this metric needs to be computed. A non-decreasing subrange is defined as
a contiguous range of indices [a,b], a<b, where each element is at least as large as the 
previous element. A non-increasing subrange is similarly defined, except each element is 
at least as large as the next. There are up to K(K−1)/2 of these respective subranges within
a window, so the metric is bounded by [−K(K−1)/2,K(K−1)/2].

Constraints
-----------
- 1≤N≤100,000 days
- 1≤K≤N days

Input Format
------------
Line 1: Two integers, N and K

Line 2: N positive integers of upvote counts, each integer less than or equal to 109

Output Format
-------------
Line 1..: N−K+1 integers, one integer for each window's result on each line


Sample Input
------------
5 3
1 2 3 1 1

Sample Output
-------------
3
0
-2

Explanation
-----------
For the first window of [1, 2, 3], there are 3 non-decreasing subranges and 0 non-increasing,
so the answer is 3. For the second window of [2, 3, 1], there is 1 non-decreasing subrange 
and 1 non-increasing, so the answer is 0. For the third window of [3, 1, 1], there is 1 
non-decreasing subrange and 3 non-increasing, so the answer is -2.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
line1 = raw_input().strip().split()
N = long(line1[0])
K = long(line1[1])
dayVotes = map(lambda x:long(x),raw_input().strip().split())

def countPerRange(sequence):

    ipArrayUP = []
    ipArrayDW = []
    
    if len(sequence) == 1:
        return 0

    if sequence[0]<=sequence[1]:
        ipArrayUP.append(0)

    if sequence[0]>=sequence[1]:
        ipArrayDW.append(0)
    
    for i in range(1,len(sequence)-1):
        if sequence[i]>=sequence[i-1] and sequence[i]>sequence[i+1]:
            ipArrayUP.append(i)
        elif sequence[i]<sequence[i-1] and sequence[i]<=sequence[i+1]:
            ipArrayUP.append(i)
    
        if sequence[i]<=sequence[i-1] and sequence[i]<sequence[i+1]:
            ipArrayDW.append(i)
        elif sequence[i]>sequence[i-1] and sequence[i]>=sequence[i+1]:
            ipArrayDW.append(i)
        
        
    if sequence[len(sequence)-1]>=sequence[len(sequence)-2]:
        ipArrayUP.append(len(sequence)-1)

    if sequence[len(sequence)-1]<=sequence[len(sequence)-2]:
        ipArrayDW.append(len(sequence)-1)

    subRangeUP = 0
    subRangeDW = 0

    if ipArrayUP != []:
        for i in range(1,len(ipArrayUP)/2+1):
            k_temp_UP = ipArrayUP[2*i-1]-ipArrayUP[2*i-2]+1
            subRangeUP += k_temp_UP*(k_temp_UP-1)/2
    else:
        subRangeUP = 0
    
    if ipArrayDW != []:
        for i in range(1,len(ipArrayDW)/2+1):
            k_temp_DW = ipArrayDW[2*i-1]-ipArrayDW[2*i-2]+1
            subRangeDW += k_temp_DW*(k_temp_DW-1)/2
    else:
        subRangeDW = 0
    
    SRTOT = subRangeUP - subRangeDW
    
    return SRTOT

for i in range(1,N-K+2):
    #print i
    seq = dayVotes[i-1:len(dayVotes)-(N-K)+i-1]
    #print seq
    ANSwer = countPerRange(seq)

    print ANSwer
