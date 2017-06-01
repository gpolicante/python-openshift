#!/usr/bin/python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello estou rodando dentro do Openshift Origin"

if __name__ == '__main__':
    app.run(debug=True,threaded=True,host="0.0.0.0",port=8080) 
