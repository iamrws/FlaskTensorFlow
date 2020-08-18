from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap

import os
import inference
import string
import random
import json
import requests
import numpy as np
import tensorflow as tf

app = Flask(__name__)
Bootstrap(app)

"""
Routes for App
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method =='POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            image_path = os.path.join('static', uploaded_file.filename)
            uploaded_file.save(image_path)
            class_name = inference.get_prediction(image_path)
            print('CLASS NAME', class_name)
            result = {
                'class_name' : class_name,
                'image_name' : image_path,
                }
            return render_template('show.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
