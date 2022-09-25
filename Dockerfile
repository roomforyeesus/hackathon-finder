FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-setuptools \
    python3-venv \
    python3-wheel \
    git \
    && rm -rf /var/lib/apt/lists/*
RUN npm install -g npm@latest
RUN apt-get install -y nodejs npm && npm install -g npm@latest docker docker-compose
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN docker-compose build
RUN docker-compose up -d
