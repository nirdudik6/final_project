#!/bin/python3.7

import os
import boto3
from time import sleep

choice=input("enter  your  choice: \n1.describe your instances\n2.install packages\n3.install netperf\n")
if choice=="1":
    client = boto3.client('ec2')
    response = client.describe_instances()
    for r in response['Reservations']:
        for i in r['Instances']:
            print("ID: " + i['InstanceId'] + "\nIP Address: " + i['PublicIpAddress'] + "\n---------------------------------------")
elif choice=="2":
    print("lets install the packages!")
    install=input("Do you want to install packages? (yes/no)\n")
    if install=="yes":
        instance=input("Which instance do you want to install the packages? (nir1/nir2)\n")
        if instance=="nir1":
            os.system('scp -i ./nir.pem ./install_packages.py ubuntu@3.21.166.235:/home/ubuntu/')
            print("run install_packages.py")
            os.system('ssh -i "nir.pem" ubuntu@ec2-3-21-166-235.us-east-2.compute.amazonaws.com')
            print("done!")
        elif instance=="nir2":
            os.system('scp -i ./nir.pem ./install_packages.py ubuntu@3.138.111.139:/home/ubuntu/')
            print("run install_packages.py")
            os.system('ssh -i "nir.pem" ubuntu@ec2-3-138-111-139.us-east-2.compute.amazonaws.com')

    else:
        print("ok if thats what you want...")

elif choice=="3":
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
else:
    print("enter 1-3 only!!!")
