from flask import Flask, url_for, redirect, render_template, flash, request
app = Flask(__name__)

import os
import json
from clarifai.client import ClarifaiApi

#setup global variables
os.environ["CLARIFAI_APP_ID"] = "MIH4l5QZirRCKb6B4HQ5pwnAqveVYD_2r460ieEn"
os.environ["CLARIFAI_APP_SECRET"] = "eNfVHLb9prAAqB6T3EVZ2masTeNCisK7dC6wsAKC"
#create our app

clarifai_api = ClarifaiApi()

@app.route('/', methods = ["POST", "GET"])
def show_result():
    print request.form
    if "linkImage" in request.form:
        linkImage = request.form["linkImage"]
        result = clarifai_api.tag_image_urls(linkImage)
    else:
        result = None
    return render_template('index.html', result = result)

if __name__ == '__main__':
    app.run(debug = True)
