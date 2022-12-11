"""
Simple app to upload an image via a web form 
and view the inference results on the image in the browser.
"""
import argparse
import io
import os
from PIL import Image

import torch
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# force_reload = recache latest code
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.eval()


@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if not file:
            return

        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        results = model([img])

        results.render()  # updates results.imgs with boxes and labels
        results.save(save_dir="static/")
        return redirect("static/image0.jpg")

    return render_template("index.html")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()

    # app.run(host="0.0.0.0", port=args.port)
    app.run(host='0.0.0.0', debug=True, port=int(os.environ.get('PORT', 5000)))
