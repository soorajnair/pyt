#! /usr/bin/python

import random
a = random.sample(list(range(0,50)),10)
b = random.sample(list(range(0,50)),10)
c=[]
print ("List 1 : "+str(a))
 
print ("List 2 : " +str(b))
for i in a : 
    if i not in b:
        c.append(i)
for j in b :
    if j not in a:
        c.append(j)
        
            
print ("common list :"+str(c)) 
