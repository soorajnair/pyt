#! /usr/bin/python
wd = raw_input("Enter a palindrom : ")
if wd == wd[::-1] :
    print(wd+" is a Palindrom")
else:
    print("This isnt a Palindrom")
