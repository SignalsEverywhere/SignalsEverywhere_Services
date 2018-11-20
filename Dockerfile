#FROM python:3.5-alpine
FROM ubuntu:latest

COPY . /app
WORKDIR /app
RUN chmod +x /app
RUN apt-get update
RUN apt-get install python3-pip python3-dev -y
RUN python3 -m pip install discord
RUN apt-get install gcc -y
RUN python3 -m pip install lxml
RUN python3 -m pip install bs4
RUN python3 -m pip install requests
RUN python3 -m pip install asyncio
CMD [ "python3", "./run.py" ]
