#!/usr/bin/env python
import boto3
ec2 = boto3.resource('ec2',region_name='us-east-1')
i=0
for instance in ec2.instances.all():
    i+=1
    print "%s.%s Status : %s" %(i,instance.id,instance.state)
