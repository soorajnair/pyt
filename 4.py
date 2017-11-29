#! /usr/bin/python
n=input("enter a number : ")
l=range(2,n)
nl=[]
for i in l:
    if n%i==0:
        nl.append(i)
print nl

