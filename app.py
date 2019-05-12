from flask import Flask, jsonify, send_file
from flask_cors import CORS
import platform

app = Flask(__name__, static_folder='dist')

# enable CORS
CORS(app)


@app.route('/json')
def get_os_name():
    p = platform.platform()
    return jsonify({'platform': p})


@app.route('/')
def index():
    vuejs_html = '/app/dist/index.html'
    return send_file(vuejs_html)
