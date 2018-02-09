#!/usr/bin/python
import boto3
import sys
import botocore

action=sys.argv[1]
bucket_name=sys.argv[2]
s3_client=boto3.client('s3')
if action=='create' :
    print "creating bucket"
    s3_client.create_bucket(Bucket=bucket_name)
s3_resource=boto3.resource('s3')
if action=='del' :
    print"deleting bucket"
    try:
        bucket=s3_resource.Bucket(bucket_name)
        for key in bucket.objects.all():
            key.delete()
        bucket.delete()
    except botocore.exceptions.ClientError as e:
        print e.responce['Error']['code']
if action=='upload' :
    print "uploading object"
    s3_resource.Object(bucket_name,'hello.txt'.put(Body=open('/tmp/hello.txt','r'))
