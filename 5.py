#! /usr/bin/python
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
for i in a : 
    if i not in b:
        c.append(i)
for j in b :
    if j not in a:
        c.append(j)
        
            
print c 
