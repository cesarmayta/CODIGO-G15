from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

#VALORES DE CONEXIÓN A MYSQL
app.config['MYSQL_HOST'] = os.environ.get("MYSQL_ADDON_HOST")
app.config['MYSQL_USER'] = os.environ.get("MYSQL_ADDON_USER")
app.config['MYSQL_PASSWORD'] = os.environ.get("MYSQL_ADDON_PASSWORD")
app.config['MYSQL_DB'] = os.environ.get("MYSQL_ADDON_DB")

mysql = MySQL(app)

@app.route('/')
def index():
    context = {
        'status':True,
        'content':'Bienvenido a mi api rest con flask y mysql'
    }
    return jsonify(context)
########## ENDPOINT ALUMNO ##############
@app.route('/alumno')
def getAlumno():
    cursor = mysql.connection.cursor()
    cursor.execute('select * from tbl_alumno')
    data = cursor.fetchall()
    cursor.close()
    context = {
        'status':True,
        'content':data
    }

    return jsonify(context)



if __name__ == "__main__":
    app.run(debug=True,port=5000)