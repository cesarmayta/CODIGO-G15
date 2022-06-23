from flask import Flask,render_template,request
from FirebaseAdmin import FirebaseAdmin

fb = FirebaseAdmin()

app = Flask(__name__)

@app.route('/')
def index():
    dicBiografia = fb.getCollection('biografia')[0]
    print(dicBiografia)
    return render_template('index.html',**dicBiografia)

@app.route('/portafolio')
def portafolio():
    listaProyectos = fb.getCollection('proyectos')
    
    context = {
        'proyectos':listaProyectos
    }

    return render_template('portafolio.html',**context)

app.run(debug=True)