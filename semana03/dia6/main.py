from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os
from os.path import join,dirname

dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#CREAMOS UNA CLASE QUE REPRENTE A UNA TABLA
class Alumno(db.Model):
    id = db.Column(db.Integer,primary_key=True) #ID INT PRIMARY_KEY
    nombre = db.Column(db.String(100),nullable=False) #nombre varchar(100)
    email = db.Column(db.String(100),unique=True) #email varchar(100)

    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email

#MIGRAMOS LAS CLASES A LA BASE DE DATOS CONVIERTIENDOLAS EN TABLAS
db.create_all()
print("se crearon las tablas en la base de datos")

############ CREAMOS LOS ESQUEMAS
ma = Marshmallow(app)
class AlumnoSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','email')

alumno_schema = AlumnoSchema()

@app.route('/')
def index():
    return jsonify({
        'status':True,
        'content':'Bienvenido a mi apirest con flask y sqlalchemy'
    })

@app.route('/alumno',methods=['POST'])
def setAlumno():
    nombre = request.json['nombre']
    email = request.json['email']

    #insertamos el registro en base de datos usando el ORM
    nuevoAlumno = Alumno(nombre,email)
    db.session.add(nuevoAlumno)
    db.session.commit()

    #seralizamos los datos para retornamos en JSON
    return alumno_schema.jsonify(nuevoAlumno)
### METODO GET PARA CONSULTAR VARIOS ALUMNOS
lista_alumnos_schema = AlumnoSchema(many=True)
@app.route('/alumno')
def getAlumno():
    listaAlumnos = Alumno.query.all() #select * from alumno
    return jsonify(lista_alumnos_schema.dump(listaAlumnos))


if __name__ == "__main__":
    app.run(debug=True,port=5000)