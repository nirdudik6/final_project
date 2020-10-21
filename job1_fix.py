#!/bin/python3.7

import os
import boto3
from time import sleep

client = boto3.client('ec2')
response = client.describe_instances()
for r in response['Reservations']:
    for i in r['Instances']:
        print("ID: " + i['InstanceId'] + "\nIP Address: " + i['PublicIpAddress'] + "\n---------------------------------------")

print("lets install the packages!")
os.system('scp -i ./nir.pem ./install_packages.py ubuntu@3.21.166.235:/home/ubuntu/')
print("run install_packages.py")
os.system('ssh -i "nir.pem" ubuntu@ec2-3-21-166-235.us-east-2.compute.amazonaws.com')
print("done!")
os.system('scp -i ./nir.pem ./install_packages.py ubuntu@3.138.111.139:/home/ubuntu/')
print("run install_packages.py")
os.system('ssh -i "nir.pem" ubuntu@ec2-3-138-111-139.us-east-2.compute.amazonaws.com')
print("done")
print("lets install netperf!")
print("lets start with nir1")
os.system('scp -i ./nir.pem ./netperf.py ubuntu@3.21.166.235:/home/ubuntu/')
print("run netperf.py")
os.system('ssh -i "nir.pem" ubuntu@ec2-3-21-166-235.us-east-2.compute.amazonaws.com')
print("lets install in nir2")
os.system('scp -i ./nir.pem ./netperf.py ubuntu@3.138.111.139:/home/ubuntu/')
print("run netperf.py")
os.system('ssh -i "nir.pem" ubuntu@ec2-3-138-111-139.us-east-2.compute.amazonaws.com')
print("done!")

