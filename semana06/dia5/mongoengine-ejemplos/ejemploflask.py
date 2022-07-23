from flask import Flask,jsonify,request
from flask_mongoengine import MongoEngine
#from marshmallow_mongoengine import ModelSchema
from marshmallow import Schema, fields
from dotenv import load_dotenv
import os
from os.path import join,dirname

import json

from bson.json_util import dumps

dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    "db": "db_demo",
}
db = MongoEngine(app)

#CREAMOS UNA CLASE QUE REPRENTE A UNA TABLA
class Alumno(db.Document):
    nombre = db.StringField()
    email = db.StringField()

############ CREAMOS LOS ESQUEMAS
#class AlumnoSchema(ModelSchema):
#    class Meta:
#        model = Alumno

#
class AlumnoSchema(Schema):
    nombre = fields.Str()
    email = fields.Str()

alumno_schema = AlumnoSchema()
alumnos_schema = AlumnoSchema(many=True)

@app.route('/')
def index():
    return jsonify({
        'status':True,
        'content':'Bienvenido a mi apirest con flask y mongoengine'
    })

@app.route('/alumno',methods=['POST'])
def setAlumno():
    nombre = request.json['nombre']
    email = request.json['email']

    #insertamos el registro en base de datos usando el ORM
    nuevoAlumno = Alumno()
    nuevoAlumno.nombre = nombre
    nuevoAlumno.email = email
    nuevoAlumno.save()
    #seralizamos los datos para retornamos en JSON
    dump_data = alumno_schema.dump(nuevoAlumno)
    return dump_data

### METODO GET PARA CONSULTAR VARIOS ALUMNOS
#lista_alumnos_schema = AlumnoSchema(many=True)
@app.route('/alumno')
def getAlumno():
    #listaAlumnos = Alumno.objects #db.alumno.find()
    lstAlumnos = []
    for usu in Alumno.objects:
        dicAlumno = {
            'nombre' : usu.nombre,
            'email' : usu.email
        }
        lstAlumnos.append(dicAlumno)

    print(lstAlumnos)
    #dump_data = alumnos_schema.dump(lstAlumnos)
    dump_data = jsonify(lstAlumnos)
    #dump_data = json.loads(dumps(Alumno.objects))

    return dump_data


if __name__ == "__main__":
    app.run(debug=True,port=5000)