from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

#VALORES DE CONEXIÓN A MYSQL
app.config['MYSQL_HOST'] = os.environ.get("MYSQL_ADDON_HOST")
app.config['MYSQL_USER'] = os.environ.get("MYSQL_ADDON_USER")
app.config['MYSQL_PASSWORD'] = os.environ.get("MYSQL_ADDON_PASSWORD")
app.config['MYSQL_DB'] = os.environ.get("MYSQL_ADDON_DB")
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

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
    cursor.execute('select alumno_id as id,alumno_nombre as nombre,alumno_email as email from tbl_alumno')
    data = cursor.fetchall()
    print(data)
    cursor.close()
    context = {
        'status':True,
        'content':data
    }

    return jsonify(context)

@app.route('/alumno',methods=['POST'])
def setAlumno():
    nombre = request.json['nombre']
    email = request.json['email']

    cursor = mysql.connection.cursor()
    cursor.execute("insert into tbl_alumno(alumno_nombre,alumno_email) values ('"+ nombre +"','"+ email +"')")

    mysql.connection.commit()

    cursor.close()

    context = {
        'status':True,
        'content':'registro exitoso'
    }

    return jsonify(context)

@app.route('/alumno/<id>')
def getAlumnoById(id):
    cursor = mysql.connection.cursor()
    cursor.execute("select * from tbl_alumno where alumno_id='"+ id +"'")

    data = cursor.fetchall()

    cursor.close()

    context = {
        'status':True,
        'content':data
    }

    return jsonify(data)

@app.route('/alumno/<id>',methods=['PUT'])
def updateAlumno(id):
    nombre = request.json['nombre']
    email = request.json['email']

    cursor = mysql.connection.cursor()
    sqlUpdateAlumno = """
    update tbl_alumno set
    alumno_nombre = '"""+ nombre + """'
    ,alumno_email = '"""+ email + """'
    where alumno_id = '"""+ id +"""'
    """
    cursor.execute(sqlUpdateAlumno)

    mysql.connection.commit()

    cursor.close()

    context= {
        'status':True,
        'content':'registro actualizado'
    }

    return jsonify(context)
    
@app.route('/alumno/<id>',methods=['DELETE'])
def deleteAlumno(id):

    try:
        cursor = mysql.connection.cursor()
        sqlDeleteAlumno = "delete from tbl_alumno where alumno_id = "+ id 

        cursor.execute(sqlDeleteAlumno)

        mysql.connection.commit()

        cursor.close()

        context = {
            'status':True,
            'content':'registro eliminado'
        }

        return jsonify(context)
    
    except Exception as err:
        context = {
            'status':False,
            'content':'error:' + err.__str__()
        }

        return jsonify(context),500

if __name__ == "__main__":
    app.run(debug=True,port=5000)