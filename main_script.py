#!/bin/python3

import subprocess  
import sys  
import os
import paramiko
from time import sleep

def menu():
    while(True):
        choice=input("enter your  choice: \n1.Discover IP\n2.install full packages centos\n3.install full packages ubuntu\n4.install jenkins master-remote\n")
        if (choice=="1"):
            Discover_ip()
        elif (choice=="2"):
            packages_centos()
        elif (choice=="3"):
            packages_ubuntu()
        elif (choice=="4"):
            install_jenkins()
        else:
            print("choose only 1-4!!!")
            continue
        if (input("do you want to exit? y/n\n") == "y"):
            break
    print("thanks and bye bye...")

def Discover_ip():
    os.system('sudo apt-get install nmap')
    ip=input("enter your local ip address+SM: (for example: 192.168.1.0/24)\n")
    print("check all the ips in network...\n")
    os.system('nmap -v -sn ' +ip)

def packages_centos():
    print("downloading python3.7...\n")
    os.system('sudo yum install gcc openssl-devel bzip2-devel libffi-devel zlib-devel')
    os.system('sudo cd /usr/src')
    os.system('sudo wget https://www.python.org/ftp/python/3.7.9/python-3.7.9.tgz')
    os.system('tar xzf python-3.7.9.tgz')
    os.system('cd python-3.7.9')
    os.system('./configure --enable-optimizations')
    os.system('make altinstall')
    os.system('rm /usr/src/python-3.7.9.tgz')
    os.system('python3.7 -v')
    print("done")
    print("installing docker...")
    os.system('sudo yum check-update')
    os.system('curl -fsSL https://get.docker.com/ | sh')
    os.system('sudo systemctl start docker')
    os.system('sudo systemctl status docker')
    os.system('sudo systemctl enable docker')
    print("done")
    print("installing ansible")
    os.system('sudo yum install epel-release')
    os.system('sudo yum install ansible')
    print("done")
    print("installing net-tools...")
    os.system('yum install network-tools')
    print("done")
    print("lets change etc/host...\n")
    host=input("enter the new host:\n")
    remote_ip=input("enter the new ip:\n")
    SetHostAt(remote_ip)
    print ("done")
    print("lets change your hostname...\n")
    os.system('sudo apt-get install systemd -y')
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

def packages_ubuntu():
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

def install_jenkins():
    print("welcome to jenkins installation :)")
    install=input("Do you want to install jenkins to another machine? (yes/no)\n")
    if install=="yes":
        username=input("enter your username:\n")
        ip=input("enter your ip address:\n")
        os.system('scp jenkins.sh ' + username + '@' + ip + ':/home/' + username)
        os.system('ssh ' + username + '@' + ip)
        print("done!")
    else:
        print("ok,as you wish...")



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


menu()
