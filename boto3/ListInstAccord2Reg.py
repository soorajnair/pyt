#! /usr/bin/python

import boto3

reg=raw_input("Enter a region : ")
try:
    ec2=boto3.client('ec2',region_name=reg)
    r = ec2.describe_instances()
    print(r)
    i=0
   # for instance in ec2.instances.all():
    #        i+=1
            
#print "%s.%s Status : %s" %(i,instance)
except:
    print "Region doesn't exist or you have misspelled it!"

