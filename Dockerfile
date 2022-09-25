FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y docker docker-compose
RUN docker-compose build
RUN docker-compose up -d
