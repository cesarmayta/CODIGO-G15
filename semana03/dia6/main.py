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



@app.route('/')
def index():
    return jsonify({
        'status':True,
        'content':'Bienvenido a mi apirest con flask y sqlalchemy'
    })

if __name__ == "__main__":
    app.run(debug=True,port=5000)