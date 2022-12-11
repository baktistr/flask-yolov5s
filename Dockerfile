FROM python:3.8-slim-buster

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

EXPOSE 5000

CMD gunicorn webapp:app