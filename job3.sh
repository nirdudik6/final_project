#!/bin/bash


echo "welcome to job3"
echo -e "how many containers do you want to create?\n"
read CONTAINERS
for i in $( eval echo {1..$CONTAINERS} )
do
    echo -e "which root do you want to use?\n"
    read root
    echo -e "which type of container do you want to create?\n"
    read machine
    if [ $machine == "dockerui" ]
    then
        sudo docker pull abh1nav/dockerui:latest
        sudo docker run -d -p $root:9000 -v /var/run/docker.sock:/docker.sock --name dockerui abh1nav/dockerui:latest -e="/docker.sock"
        echo "DONE!"

    else
        sudo docker run -d -p $root:8080 $machine
        echo "done!"
    fi
done
sudo docker ps
echo -e "which kind of image do you want to download?\n"
read IMAGE
echo "this is the available images:"
sudo docker search $IMAGE
echo -e "which image's ID do you want to download?\n"
read download
sudo docker pull $download
echo "DONE!"
sudo docker images
echo -e "Do you want to remove container or image?\n"
read REMOVE
if [ $REMOVE == "container" ]
then
    echo "There are the existing containers:"
    sudo docker ps -a
    echo -e "Enter the container's id you want to remove:\n"
    read id 
    sudo docker stop $id
    sudo docker rm $id
    echo "done!"
    sudo docker ps -a
elif [ $REMOVE == "image" ]
then
    echo "There are the existing images:"
    sudo docker images
    echo -e "Enter the image's id you want to remove:\n"
    read id1
    sudo docker rmi $id1
    echo "done!"
    sudo docker images
fi
