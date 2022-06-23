from flask import Flask,render_template,request,session
from FirebaseAdmin import FirebaseAdmin

fb = FirebaseAdmin()

app = Flask(__name__)

#creamos una clave secreta para las variables de sesión
app.secret_key = 'qwerty123456'

@app.route('/')
def index():
    dicBiografia = fb.getCollection('biografia')[0]
    session['biografia'] = dicBiografia

    return render_template('index.html')

@app.route('/portafolio')
def portafolio():
    listaProyectos = fb.getCollection('proyectos')
    
    context = {
        'proyectos':listaProyectos
    }

    return render_template('portafolio.html',**context)

@app.route('/acercade')
def acercade():
    return render_template('acercade.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

app.run(debug=True)