#!/bin/python3

import os
import boto3
from time import sleep


print("creating 2 instances!")
ec2 = boto3.resource('ec2')

# create a new EC2 instance
instances = ec2.create_instances(
ImageId=input("enter you image id:\n"),
MinCount=1,
MaxCount=2,
InstanceType='t2.micro',
KeyName=input("enter the keyname:\n")
)

print("done!")
print("installing all packages!")
print("lets install python3.7...")
os.system('sudo apt update')
os.system('sudo apt install software-properties-common')
os.system('sudo add-apt-repository ppa:deadsnakes/ppa')
os.system('sudo apt update')
os.system('sudo apt install python3.7')
os.system('sudo python ––version')
print("done")
print("lets install docker...")
os.system('sudo curl -fsSL https://get.docker.com -o get-docker.sh')
os.system('sudo sh get-docker.sh')
print("done")
print("lets install ansible...")
os.system('sudo apt update')
os.system('sudo apt install software-properties-common')
os.system('sudo apt-add-repository --yes --update ppa:ansible/ansible')
os.system('sudo apt install ansible')
print("done")
print("lets install net-tools...")
os.system('sudo apt-get update -y')
os.system('sudo apt-get install -y net-tools')
print("done")
print("lets change the etc hosts...")
host=input("enter the new host:\n")
remote_ip=input("enter the new ip:\n")
SetHostAt(remote_ip)
print("done")
print("lets change your hostname!\n")
os.system('apt-get install systemd -y')
new_hostname=input("enter your new hostname:\n")
os.system('sudo hostnamectl set-hostname ' + new_hostname)
os.system('hostnamectl')
print("this is your new hostname:\n")
os.system('hostname')
print("lets change your root password!")
dilema=input("Are you sure you want to change your root password? y/n\n")
if (dilema=="y"):
    os.system('sudo passwd root')
    print("DONE!")
elif (dilema=="n"):
    print("ok,you don't want to change...")
print("done!")
print("installing netperf!")
os.system('sudo apt-get update -y')
os.system('sudo apt-get install -y netperf')
print("done!")

def SetHostAt(remote_ip):
    MYROOT = '/'
    a = augeas(root=MYROOT)
    matches=input("Do you have an exists records? yes/no\n")
    if (matches=="yes"):
        index = matches[0].split('/')[4]
        record_exists = True
        print(index)
    elif (matches=="no"):
        record_exists = False
        index = len(a.match("/files/etc/hosts/*"))
        print(index)
    a.set("/files/etc/hosts/%s/ipaddr" % index, remote_ip)
    a.set("/files/etc/hosts/%s/canonical" % index, host)
    a.save()
    msg = "set host ip to %s" % remote_ip
    init("server checker")
    notification("server checker", mgs).show()
