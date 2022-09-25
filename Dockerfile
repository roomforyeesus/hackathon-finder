FROM ubuntu:latest
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y docker-compose-plugin docker
RUN docker-compose build
RUN docker-compose up -d
