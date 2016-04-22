from flask import Flask, url_for, redirect, render_template, flash
app = Flask(__name__)

import os
import json
from clarifai.client import ClarifaiApi

#setup global variables
os.environ["CLARIFAI_APP_ID"] = "MIH4l5QZirRCKb6B4HQ5pwnAqveVYD_2r460ieEn"
os.environ["CLARIFAI_APP_SECRET"] = "eNfVHLb9prAAqB6T3EVZ2masTeNCisK7dC6wsAKC"
#create our app

clarifai_api = ClarifaiApi()
result = clarifai_api.tag_image_urls('http://img10.deviantart.net/2a92/i/2011/161/6/e/sweet_grin_by_sweetgrinplz-d3ilgeq.png')
#parsed = json.loads(result)
print json.dumps(result, indent = 4, sort_keys = True)

@app.route('/')
def index():
    return render_template('index.html', result = result)

@app.route('/result')
def returnResult():
    return result

if __name__ == '__main__':
    app.run()
