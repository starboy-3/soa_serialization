FROM ubuntu:bionic

WORKDIR /service

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python-pip
RUN python3 -m pip install -r requirements.txt
COPY . .