from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'status':True,
        'content':'Bienvenido a mi apirest con flask y sqlalchemy'
    })

if __name__ == "__main__":
    app.run(debug=True,port=5000)