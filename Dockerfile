FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release 
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
RUN apt-get update
RUN apt-get install -y docker docker-compose
RUN docker-compose build
RUN docker-compose up -d
