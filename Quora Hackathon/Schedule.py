"""
SCHEDULE
********

Problem Statement
-----------------
At Quora, we run all our unit tests across many machines in a test cluster on every code push.

One day, we decided to see if we could optimize our test cluster for cost efficiency by using
only one machine to run all N tests.

Suppose we know two things about each test: the time needed to run this test, Ti, and the 
probability that this test will pass, Pi.

Given these as input, come up with the minimum expected time (based on the optimal ordering 
of the tests) of getting “go or no go” feedback on the code push, i.e. the expected time when
we understand that either i) at least one test has failed, or that ii) all tests have passed.

Constraints
-----------
- Accuracy threshold for evaluating floats: 10−6
- 1≤N≤100
- 1≤Ti≤100
- 0≤Pi≤1

Input Format
------------
Line 1: One integer N

Line 2..N+1: One integer Ti and one float Pi separated by one space.

Output Format
-------------
Line 1: One float, the minimum expected time


Sample Input
------------
3
3 0.1
7 0.5
9 0.2

Sample Output
-------------
4.04

"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# Functions Needed
def prob_eq(per_times, per_pr):
    # Probability Terms
    if N == 1:
        terms_p = [min([1 - per_pr[0],per_pr[0]])]
    elif N >= 2:
        terms_p = [1 - per_pr[0], per_pr[0]]

    for i in range(2,N):
        terms_p.append(terms_p[-1]*per_pr[i-1])
        terms_p[-2] = terms_p[-2]*(float(1)-per_pr[i-1])
    
    # Sum Terms
    terms_sum = [per_times[0]]
    for i in range(1,N):
        terms_sum.append(terms_sum[-1]+per_times[i])

    # Final Equation Terms
    eq_terms = []
    for i in range(0,N):
        eq_terms.append(terms_p[i]*terms_sum[i])

    print per_times, per_pr, eq_terms, sum(eq_terms)
    # Final Answer
    return sum(eq_terms)

def permutate(seq):
    """permutate a sequence and return a list of the permutations"""
    if not seq:
        return [seq] # is an empty sequence
    else:
        temp = []
        for k in range(len(seq)):
            part = seq[:k] + seq[k+1:]
            #print k, part # test
            for m in permutate(part):
                l = seq[k:k+1] + m
                temp.append(l)
                #print m, seq[k:k+1], temp # test
        return temp
    
#======================================
# Parse Input
N = int(raw_input())
input_data = []
for i in range(0,N):
    temp_data = raw_input().strip().split()
    temp_data[0] = int(temp_data[0])
    temp_data[1] = float(temp_data[1])
    temp_data = tuple(temp_data)
    input_data.append((temp_data))
    
# Build all posible permutations    
per_data = permutate(input_data)

# Solve for all posibilities and find the minimum value
min_exp_time = sys.maxint  
for j in range(0,len(per_data)):
    t = [row[0] for row in per_data[j]]
    p = [row[1] for row in per_data[j]]
    att_j = prob_eq(t, p)
    if att_j < min_exp_time:
        min_exp_time = att_j

# Print Answer
print min_exp_time