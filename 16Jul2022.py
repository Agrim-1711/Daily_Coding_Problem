#DCP 16-Jul-22: Program to calculate the value of Pi using Monte-Carlo

import random
import time
start=time.time()
blist=[]
for i in range(1,1000001):
  alist = [random.random(), random.random()]
  blist.append(alist)
#print(blist)

incircle=0
points=0
for x in blist:
    r=pow(x[0]*x[0]+x[1]*x[1],0.5)
    points +=1
    if r<=1:
        incircle +=1
end=time.time()
print(points,"points, pi=",4*incircle/points,",",end-start,"sec")