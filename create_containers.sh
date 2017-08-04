#!/bin/bash
# written by me
# thanks God
#
# isaccavalcante AT alu DOT ufc DOT br

# Useful docker commands:
#docker network ls
#docker ps
#docker inspect CONTAINER_ID --format '{{ .NetworkSettings.IPAddress }}' #pocket
#docker-machine ls
#

# Creating and starting swarm manager
docker-machine create --driver virtualbox manager1
docker-machine start manager1

# Creating and starting swarm workers through a loop
for i in $(seq 2 10) ; do
	docker-machine create --driver virtualbox worker$i;
	docker-machine start worker$i;
done




