from flask import Flask, jsonify, request, send_file
from PIL import Image
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Image Converter API!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
