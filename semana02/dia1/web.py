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

@app.route('/suma')
def suma():
    n1 = request.args.get('n1','0')
    n2 = request.args.get('n2','0')
    resultado = int(n1) + int(n2)
    return '<center><b>la suma de {} + {} es {}</b></center>'.format(n1,n2,resultado)

@app.route('/resta/<int:n1>/<int:n2>')
def resta(n1=0,n2=0):
    resultado = n1 - n2
    return '<center><b>la resta de {} - {} es {}</b></center>'.format(n1,n2,resultado)

app.run(debug=True)

