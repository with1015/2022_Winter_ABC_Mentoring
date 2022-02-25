FROM python:3.6
MAINTAINER ABC_MENTORING "ABC@unist.ac.kr"

RUN apt-get update
RUN apt-get upgrade

COPY . /app

WORKDIR /app/web_benchmark

RUN pip3 install Django

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0:8000"]
