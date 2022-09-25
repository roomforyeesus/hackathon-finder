FROM ubuntu:latest
RUN docker-compose build
RUN docker-compose up -d
