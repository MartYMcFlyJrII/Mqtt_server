# Mqtt_server
The purpose of this project is to receive the values from 4 sensors and send messages to different social networks warning the user that the limit has been exceeded, using Node-red with docker.

Commands Docker:
Teammates: 
(For first time)
docker-compose up -- build -d

(for regular use) 
1- to turn on the server
  docker-compose up

2- to turn it down without deleting the data
  docker-compose down

3- to delete the data saved
  docker volume prune (and select "yes")

4- use again 
  docker-compose up --build -d 
