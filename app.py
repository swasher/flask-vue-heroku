from flask import Flask, jsonify
from flask_cors import CORS
import platform

app = Flask(__name__)

# enable CORS
CORS(app)

@app.route('/')
def get_os_name():
    p = platform.platform()
    return jsonify({'platform': p})
