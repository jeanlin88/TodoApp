FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install python3.8 -y && \
    apt-get install python3-pip -y && \
    pip3 install --upgrade pip

RUN useradd -ms /bin/bash myuser
USER myuser

RUN mkdir /home/myuser/myapp
WORKDIR /home/myuser/myapp

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "./start.sh" ]