# Mqtt_server

The purpose of this project is to receive the values from 4 sensors and send messages to different social networks warning the user that the limit has been exceeded, using Node-red with docker.

# IMPORTANT

If you have changes in the Node-red that you want to commit, pls use this command first:

```
$ docker cp  Node-red:/data  ./node_red
```

# **Commands Docker:**

## Docker-compose: (TEAMMATES THIS IS EASIER)

##### ***(For the first time or you use git pull)***

```
$ docker-compose up --build 
```

##### (NOT the first time)

1- To turn on the server

```
$ docker-compose up
```

2- To turn it down without deleting the data

```
docker-compose down
```

3- Extras commands

If you want to use the terminal of a specific container (virtual machine). After you use the docker-compose up command you can use:

```
docker-compose exec nodered sh
```

If you want to use the same terminal use -d at the end

```
$ docker-compose up -d
```

*All commands:*

```
$ docker-compose -h 

Commands:
  build       Build or rebuild services
  convert     Converts the compose file to platform's canonical format
  cp          Copy files/folders between a service container and the local filesystem
  create      Creates containers for a service.
  down        Stop and remove containers, networks
  events      Receive real time events from containers.
  exec        Execute a command in a running container.
  rm          Removes stopped service containers
  run         Run a one-off command on a service.
  start       Start services
  stop        Stop services
  top         Display the running processes
  unpause     Unpause services
  up          Create and start containers
  version     Show the Docker Compose version information
```


## Docker

1- **Simplest form to run node-red is:**

```
$ docker run -it -p 1880:1880 -v node_red_data:/data --name mynodered nodered/node-red:latest
```

explanation of this command:

```
$ docker run              - run this container, initially building locally if necessary
    -it                     - attach a terminal session so we can see what is going on
    -p 1880:1880            - connect local port 1880 to the exposed internal port 1880
    -v node_red_data:/data  - mount a docker named volume called `node_red_data` to the container /data directory so any changes made to flows are persisted
    --name mynodered        - give this machine a friendly local name
    nodered/node-red        - the image to base it on - currently Node-RED v1.2.0
```

2- Stop docker container:

```
$ docker stop mynodered
```

3- Backup data

To save the flow of node-red container you can use a docker tool called volumes:

```
$ docker volume create --name node_red_data
$ docker volume ls
DRIVER              VOLUME NAME
local               node_red_data
$ docker run -it -p 1880:1880 -v node_red_data:/data --name mynodered nodered/node-red
```

If you need to backup the data from the mounted volume you can access it while the container is running.

```
$ docker cp  name_of_the_container:/data  /your/backup/directory
```

Using Node-RED to create and deploy some sample flows, we can now destroy the container and start a new instance without losing our user data.

```
$ docker stop mynodered
$ docker rm mynodered
$ docker run -it -p 1880:1880 -v node_red_data:/data --name mynodered nodered/node-red
```

When you redeploy with run, all the previous changes are saved.

3- T**o delete the data saved**

```
$ docker volume rm node_red_data
```

This command is going to remove only the node_red_data volume

```
$ docker volume prune (and select "yes")
```

This command is going to remove all unused volumes, be careful.
