from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017')

db_codigo = cliente['db_codigo']

colAlumno = db_codigo['alumno']

"""
dicNuevoAlumno = {
    "id":2,
    "nombre":"carlos paredes",
    "email":"carlosparedes@gmail.com",
    "celular":"23322323",
    "github":"https://www.github.com/cparedes"
}

nuevoAlumnoId = colAlumno.insert_one(dicNuevoAlumno)

print("nuevo alumno" + str(nuevoAlumnoId))
"""
for alumno in colAlumno.find():
    print(alumno['nombre'] + ' - ' +  alumno['email'] + ' - ' + alumno['celular'])
