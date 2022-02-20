FROM ubuntu:16.04

MAINTAINER Hyunjoon_Jeong "with1015@unist.ac.kr"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /app

WORKDIR /app

ENTRYPOINT ["python"]
CMD ["hello_world.py"]
