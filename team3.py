# The binomial coefficient (n,k) is the number of ways of 
# picking k unordered outcomes from n possibilities:
# n!/((n-k)!*k!).
# In mathematics, the factorial of a non-negative integer n, 
# denoted by n!, is the product of all positive integers 
# less than or equal to n:
# n! = n⋅(n−1)⋅(n−2)⋅(n−3) ⋅ ⋯ ⋅ 3 ⋅ 2 ⋅ 1 . 
# Selecting 5 members with 8 complementary skills among 
# 30 members means that there are 142506 candidates.
# 30!/((5!)*(25!))=142506
# Selecting 5 members among 1000 members 
# 1000!/((995!)*(5!))=8250291250200=8.2*10^12 tera candidates
# 1000!/((994!)*(6!))=1368173298991500=1.3*10^15 peta candidates
# the goal is to find the best or nearly best candidate.
# Selection is based on mutually complementary skills.
# Skills are represented by an 8 dimentional vector.
# It means that selected 5 members with skils should be mutually
# orthogonal. 
# Penalty is a sum of absolute dot product of all pairs. 
# There are 10 pairs in 5 members.
# There are 15 pairs in 6 members.

import random
from random import sample
totalmembers=1000
selectedmembers=5
skills=8
low=-1
high=2
th=1
humans={}
members=[]
random.seed(8)
for i in range(totalmembers):
 members.append(i)
strng='humans[str(i)]=str(random.randrange(low,high))'
for i in range(skills-1):
 strng=strng+'+str(random.randrange(low,high))'
print(strng)
def mem():
 for i in range(totalmembers):
  exec(strng) 
 print(humans)
from itertools import combinations
L=[]
for i in range(selectedmembers):
 L.append(i)
com=[",".join(map(str, comb)) for comb in combinations(L, 2)]

def cal(lef,rgh):
 left=sel[lef]
 right=sel[rgh]
 leftnum=[]
 plus=''
 for i in range(len(left)):
  if left[i]=='-':
   plus='-'
  else:
   leftnum.append(plus+left[i])
   plus=''
 rightnum=[]
 plus=''
 for i in range(len(right)):
  if right[i]=='-':
   plus='-'
  else:
   rightnum.append(plus+right[i])
   plus=''
 calc=0
 for i in range(skills):
  calc=calc+int(leftnum[i])*int(rightnum[i])
 return int(calc)

select=[]
sel=[]
def init(index):
 select=sample(members,selectedmembers)
 for i in select:
  sel.append(humans[str(i)])
 return select
def run(index,select):
 orth=0
 for i in range(len(com)):
  lef=com[i].split(',')[0]
  rgh=com[i].split(',')[1]
  c=cal(int(lef),int(rgh))
  if c>=th:orth=c;break
  orth=orth+abs(c)
 if orth==0:
  print('select=',select)
  print('sel=',sel)
  print('ortho=0',index)
  print('')
# if orth==1:
#  print('sel=',sel)
#  print('ortho=1',index)
#  print('')
# if orth==2:
#  print('sel=',sel)
#  print('ortho=2',index)
 his.append(orth)
his=[]
mem()
import sys
trials=int(sys.argv[1])
for i in range(trials):
 select=init(i)
 run(i,select)
 sel=[]
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
min=min(his)
minindex=his.index(min)
min=str(min)
minindex=str(minindex)
#print('total members=',totalmembers,'selected member',selectedmembers,'trials=',trials,'ortho=',min+' '+'index=',minindex)
'''
plt.hist(his,bins=50)
plt.text(20,trials/15,'ortho='+min+' '+minindex)
plt.xlabel('orthogonality')
plt.ylabel('the number of times')
plt.savefig('orthogonal.png')
plt.show()
print(pd.DataFrame(his).value_counts())
'''
