from flask import Flask, jsonify, send_file
from flask_cors import CORS
import platform

app = Flask(__name__, static_folder='dist/static')

# enable CORS
CORS(app)

import os

@app.route('/json')
def get_os_name():
    p = platform.platform()
    return jsonify({'platform': p})

@app.route('/')
def index():
    dist_dir = '/app/dist'
    entry = os.path.join(dist_dir, 'index.html')
    return send_file(entry)
