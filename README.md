# README.md

@TODO

#### Useful docker comands and legend

* Showing all IP addresses of running containers
```docker ps -q | xargs docker inspect --format '{{ .NetworkSettings.IPAddress }}'
```

* Showing all MAC addresses of running containers
```docker ps -q | xargs docker inspect --format '{{ .NetworkSettings.MacAddress }}'
```

* Running an alpine container in background
```docker run -d alpine
```

* Listing network informations about docker containers
```docker network ls
```

* Listing docker runnining containers
```docker ps
```

* Stopping all containers
```docker stop $(docker ps -a -q)
```

* Deleting all containers
```docker rm $(docker ps -a -q)
```
