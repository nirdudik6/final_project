#!/bin/bash

sudo apt-get update -y
sudo apt install openssh-server -y
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.7
sudo python ––version
echo "lets change your hostname!"
sudo apt-get install systemd -y
echo -e "enter your new hostname:\n"
read hostname
sudo hostnamectl set-hostname $hostname
hostnamectl
echo "this is your new hostname:"
hostname
sudo visudo
sudo nano /etc/hosts
ssh-keygen -t rsa
echo -e "enter your key name:\n"
read keyname
echo -e "enter your user:\n"
read user
echo -e "enter your host:\n"
read host
ssh-copy-id -i $keyname $user@$host
