"""
ONTOLOGY
********

Problem Statement
-----------------
Quora has many questions on different topics, and a common product use-case for our 
@mention selectors and search service is to look-up questions under a certain topic 
as quickly as possible.

For this problem, imagine a simplified version of Quora where each question has only 
one topic associated with it. In turn, the topics form a simplified ontology where 
each topic has a list of children, and all topics are descendants of a single root 
topic.

Design a system that allows for fast searches of questions under topics. There are N 
topics, M questions, and K queries, given in this order. Each query has a desired topic
as well as a desired string prefix. For each query, return the number of questions that 
fall under the queried topic and begin with the desired string. When considering topics, 
we want to include all descendants of the queried topic as well as the queried topic 
itself. In other words, each query searches over the subtree of the topic.

The topic ontology is given in the form of a flattened tree of topic names, where each
topic may optionally have children. If a topic has children, they are listed after it 
within parentheses, and those topics may have children of their own, etc. See the sample 
for the exact input format. The tree is guaranteed to have a single root topic.

For ease of parsing, each topic name will be composed of English alphabetical characters,
and each question and query text will be composed of English alphabetical characters, 
spaces, and question marks. Each question and query text will be well behaved: there will 
be no consecutive spaces or leading/trailing spaces. All queries, however, are case 
sensitive.

Constraints
-----------
- For 100% of the test data, 1≤N,M,K≤105 and the input file is smaller than 5MB

- For 50% of the test data, 1≤N,M,K≤2⋅104 and the input file is smaller than 1MB

Input Format
------------
- Line 1: One integer N

- Line 2: N topics arranged in a flat tree (see sample)

- Line 3: One integer M

- Line 4...M+3: Each line contains a topic name, followed by a colon and a space, and then
  the question text.

- Line M+4: One integer K

- Line M+5...M+K+4: Each line contains a topic name, followed by a space, and then the 
  query text.

Output Format
-------------
- Line 1...K: Line i should contain the answer for the ith query.


Sample Input
------------
6
Animals ( Reptiles Birds ( Eagles Pigeons Crows ) )
5
Reptiles: Why are many reptiles green?
Birds: How do birds fly?
Eagles: How endangered are eagles?
Pigeons: Where in the world are pigeons most densely populated?
Eagles: Where do most eagles live?
4
Eagles How en
Birds Where
Reptiles Why do
Animals Wh

Sample Output
-------------
1
2
0
3

Explanation
-----------
The first query corresponds to the green area in the diagram, since it is looking for
topics under Eagles, and the query string matches just one question: "How endangered 
are eagles?" The second query corresponds to the blue area in the diagram, which is the 
subtree of Birds, and matches two questions that begin with "Where". The third corresponds 
to the red area, which does not have any questions that begin with "Why do". The final 
query corresponds to the entire tree, since Animals is the root topic, and matches three 
questions. 

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
class node(object):
    def __init__(self, value, level, children = []):
        self.value = value
        self.children = children
        self.lvl = level
    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.lvl)+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret
    
       
N = raw_input()
pre_tree = raw_input().strip().split()
M = long(raw_input())
quest = []
for i in range(0,M):
    pre_quest = raw_input().strip().split(': ')
    quest.append((pre_quest[0],pre_quest[1])) 
K = long(raw_input())
queries = []
for i in range(0,K):
    searchItems = raw_input().strip().split()
    queries.append((searchItems[0], ' '.join(searchItems[1:len(searchItems)])))
    
for i in range(0,len(pre_tree)):
    # At step i = 0 We initialize the tree
    # and the Variables we will need later
    if i == 0:
        doorCount = -1                                  # Initial level (-1 is used only to initialize variable)
        idCode = str(doorCount+2)
        groot = node(pre_tree[i],idCode,[])             # Tree root. First element
        id_Terms = [(idCode, pre_tree[i])]
        groot_Path = [groot]                            # Initialize path array with the root
        childCount = []                                 # Initialize array that will store the # of children per level
     
    # If there is a '(', we need move one level down.
    elif pre_tree[i] == '(':
        doorCount += 1                                   # Update level     
        childCount.append(0)                             # New child 'space' opened            
        idCode = idCode + str(childCount[doorCount])     # New idCode
        groot_curr_loc = groot_Path[doorCount].children  # Current position = New 'Child Space'
    
    # If there is a ')', we need move one level up.
    elif pre_tree[i] == ')':                                                   
        idCode = idCode[:doorCount]
        doorCount -= 1                                   # Update level
        idCode = idCode + str(childCount[doorCount])
        groot_curr_loc = groot_Path[doorCount].children  # Update Current position = Previous 'Child Space'
            
    # Time to add the newborn child
    else:
        idCode = idCode[:doorCount+1]
        idCode = idCode + str(long(childCount[doorCount]+1))
        groot_curr_loc.append(node(pre_tree[i],idCode,[]))     						# New node method
        id_Terms.append((idCode, pre_tree[i]))
        groot_Path = groot_Path[:doorCount+1]                   					# Chop the useless part of the path.
        groot_Path.append(groot_Path[doorCount].children[childCount[doorCount]])    #Update path
        childCount[doorCount] += 1                              					# Update childcount for this level
        childCount = childCount[:doorCount+1]                   					# Chop the useless part of the childcount array.
        idCode = idCode[:doorCount+1]
        idCode = idCode + str(childCount[doorCount])
        

for i in range(0, len(quest)):        
    ind = [x for x, y in enumerate(id_Terms) if y[1] == quest[i][0]] 
    a = list(quest[i])
    a.insert(0, id_Terms[ind[0]][0])
    quest[i] = tuple(a)

quest = sorted(quest, key=lambda x: x[0])
    
for i in range(0, len(queries)):
    ind = [x for x, y in enumerate(id_Terms) if y[1] == queries[i][0]] 
    a = list(queries[i])
    a.insert(0, id_Terms[ind[0]][0])
    queries[i] = tuple(a)
    
for j in range(0, len(queries)):
    counter = 0
    for i in range(0, len(quest)):
        if queries[j][2] == "":
            counter = 0
        elif queries[j][0] == quest[i][0][:len(queries[j][0])] and queries[j][2] == quest[i][2][:len(queries[j][2])]:
            counter += 1
    print counter