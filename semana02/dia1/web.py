#primera app web con flask
from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    return '<center><h1>BIENVENIDO CESAR MAYTA</h1></center>'

@app.route('/saludo')
def saludo():
    nombre = request.args.get('nombre','no hay nombre')
    return '<center><b>Hola {}</b></center>'.format(nombre)

app.run(debug=True)

