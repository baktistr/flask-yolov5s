# Yolov5 object detection model deployment using Flask

This repo contains example apps for exposing the [yolo5](https://github.com/ultralytics/yolov5) object detection model from [pytorch hub](https://pytorch.org/hub/ultralytics_yolov5/) via a [flask](https://flask.palletsprojects.com/en/1.1.x/) api/app.

## Live Demo

https://yolov5s-flask.herokuapp.com/

## Web app

Simple app consisting of a form where you can upload an image, and see the inference result of the model in the browser. Run:

`$ python3 webapp.py --port 5000`

then visit http://localhost:5000/ in your browser:

<p align="center">
<img src="https://github.com/baktistr/yolov5-flask/blob/master/docs/screenshoot1.png" width="450">
</p>

<p align="center">
<img src="https://github.com/baktistr/yolov5-flask/blob/master/docs/screenshoot2.png" width="450">
</p>

## Run locally

Run app via python web server:

`$ python3 webapp.py --port 5000`

then visit http://localhost:5000/ in your browser

## Docker

This Repo is for deployment using Docker on Heroku

## reference

- https://github.com/ultralytics/yolov5
- https://github.com/robmarkcole/yolov5-flask (this repo was forked from here)
