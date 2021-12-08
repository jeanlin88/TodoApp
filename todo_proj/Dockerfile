FROM ubuntu:18.04

ENV PYTHONUNBUFFERRED 1

RUN apt-get update -y
RUN apt-get install python3.8 -y
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade pip

RUN useradd -ms /bin/bash myuser
USER myuser

RUN mkdir /home/myuser/myapp
WORKDIR /home/myuser/myapp

COPY . .

RUN pip3 install -r requirements.txt

CMD ./start.sh