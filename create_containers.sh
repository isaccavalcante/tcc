#!/bin/bash
# written by Isac C.
# thanks God
#
#
echo "[+] Running containers"

docker run -td alpine > /dev/null
printf "\r[+] created 1 container" 

for i in $(seq 2 10); do
	docker run -td alpine > /dev/null
	printf "\r[+] created $i containers" 
done

echo
echo -e "IP Address\tMAC Address"
paste <(docker ps -q | xargs docker inspect --format '{{ .NetworkSettings.IPAddress }}') \
      <(docker ps -q | xargs docker inspect --format '{{ .NetworkSettings.MacAddress }}')

echo "[-] Stopping containers..."
docker stop $(docker ps -a -q) > /dev/null
echo "[-] Deleting containers..."
docker rm $(docker ps -a -q) > /dev/null
echo "[+] Execution finished"

# Useful docker comands and legend

# Showing all IP addresses of running containers
#docker ps -q | xargs docker inspect --format '{{ .NetworkSettings.IPAddress }}' 

# Showing all MAC addresses of running containers
#docker ps -q | xargs docker inspect --format '{{ .NetworkSettings.MacAddress }}' 

# Running an alpine container in background
#docker run -td alpine

# Listing network informations about docker containers
#docker network ls 

# Listing docker runnining containers
#docker ps 

# Stopping all containers
#docker stop $(docker ps -a -q) 

# Deleting all containers
#docker rm $(docker ps -a -q) 
