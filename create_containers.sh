#!/bin/bash
# written by me
# thanks God
#
# isaccavalcante AT alu DOT ufc DOT br

# Useful docker commands:
#docker network ls
#docker ps
#docker inspect CONTAINER_ID --format '{{ .NetworkSettings.IPAddress }}' #pocket


# Creating swarm manager
docker-machine create --driver virtualbox manager1

# Creating swarm workers through a loop
for i in $(seq 2 10) ; do
	docker-machine create --driver virtualbox worker$i;
done


