#!/usr/bin/env python
import boto.ec2 
from boto.ec2 import EC2Connection
 
csv_file = open('instances.csv','w+')
 
def process_instance_list(connection):
    map(build_instance_list,connection.get_all_instances())
 
def build_instance_list(reservation):
    map(write_instances,reservation.instances)
 
def get_tag(tags, tag_name):
    if tag_name in tags.keys():
        return tags[tag_name]
    else:
        return "N/A"
 
def write_instances(instance):

    csv_file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%("Project",
                                                        "Name",
                                                        "private_ip_address",
                                                        "EnvType",
                                                        "instance_type",
                                                        "key_name",
                                                        "OS",
                                                        "placement",
                                                        "subnet_id",
                                                        "vpc_id"))
 
    csv_file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(get_tag(instance.tags, "Project"),
                                                         get_tag(instance.tags, "Name"),
                                                         instance.private_ip_address,
                                                         get_tag(instance.tags, "EnvType"),
                                                         instance.instance_type,
                                                         instance.key_name,
                                                         get_tag(instance.tags, "OS"),
                                                         instance.placement,
                                                         instance.subnet_id,
                                                         instance.vpc_id))
    csv_file.flush()
 
 
if __name__=="__main__":
    connection = boto.ec2.connect_to_region("us-east-1")
    process_instance_list(connection)
    csv_file.close()
