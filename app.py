#!/usr/bin/python

from flask import Flask, render_template, request, session
import os

app = Flask(__name__)
app.secret_key = "!@:L#J!:Ljasdas"

@app.route("/",methods=["GET","POST"])
def index():
    if not "usuario" in session.keys():
        usuario = ""
    else:
        usuario = session["usuario"]
    if (request.method == "POST"):
        foto = request.files["foto"]
        foto.save(os.path.abspath(os.path.dirname(__file__))+"/static/imagens/%s"%foto.filename)
    fotos = os.listdir(os.path.abspath(os.path.dirname(__file__))+"/static/imagens/")
    var1 = os.environ["var1"]
    var2 = os.environ["var2"]
    return render_template("index.html",fotos=fotos,usuario=usuario,var1=var1,var2=var2)
    
@app.route("/login")
def login():
    session["usuario"] = "alisson"
    return "logado"


@app.route("/logout")
def logout():
    session.pop("usuario")
    return "deslogado"
    
if __name__ == '__main__':
    app.run(debug=True,threaded=True,host="0.0.0.0",port=8080) 
