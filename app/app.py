#!/home/miyablo/.pyenv/versions/3.7.0/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from apis.sample import sample_module

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=['GET'])
def root():
    response_data = {}
    response_data["status"] = "200"
    response_data["message"] = "running"
    return(jsonify(response_data))

@app.route('/hello', methods=['GET'])
def hello():
    response_data = {}
    response_data["status"] = "200"
    response_data["message"] = "Hello World!"
    return(jsonify(response_data))

app.register_blueprint(sample_module)

if __name__ == '__main__':
    app.run()