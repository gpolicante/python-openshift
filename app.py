#!/usr/bin/python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Fazendo teste no minishift"

if __name__ == '__main__':
    app.run(debug=True,threaded=True,port=8080) 
