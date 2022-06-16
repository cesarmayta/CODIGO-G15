#LIBRERIA DE CRUD
############# FUNCIONES ###############
def buscarAlumno(valorBusqueda,listaAlumnos):
    indiceAlumno = -1
    for indice in range(len(listaAlumnos)):
        alumno = listaAlumnos[indice]
        for clave,valor in alumno.items():
            if(clave == "email" and valor == valorBusqueda):
                indiceAlumno = indice
                break
    return indiceAlumno

def menu():
    print(
    """
    ===============================================================
                SISTEMA DE MATRICULA DE ALUMNOS
    ===============================================================
    [1] REGISTRAR ALUMNO
    [2] MOSTRAR ALUMNOS
    [3] ACTUALIZAR ALUMNO
    [4] ELIMINAR ALUMNO
    [5] SALIR DEL SISTEMA
    ===============================================================
    """)

def insertarAlumno(alumnos):
    nombre = input("NOMBRE : ")
    email = input("EMAIL : ")
    celular = input("CELULAR : ")
    dictNuevoAlumno = {
            'nombre':nombre,
            'email':email,
            'celular':celular
    }
    alumnos.append(dictNuevoAlumno)

def actualizarAlumno(indiceAlumno,alumnos):
    print("alumno a editar : " + alumnos[indiceAlumno].get("nombre"))
    print("NUEVOS VALORES PARA EL ALUMNO : ")

    nombre = input("NOMBRE ("+ alumnos[indiceAlumno].get("nombre") +") : ")
    if(nombre == ''):
        nombre = alumnos[indiceAlumno].get("nombre")
    email = input("EMAIL ("+ alumnos[indiceAlumno].get("email") +") : ")
    if(email == ''):
        email = alumnos[indiceAlumno].get("email")
    celular = input("CELULAR ("+ alumnos[indiceAlumno].get("celular") +") : ")
    if(celular == ''):
        celular = alumnos[indiceAlumno].get("celular")
    
    dictAlumnoEditar = {
        'nombre':nombre,
        'email':email,
        'celular':celular
    }

    alumnos[indiceAlumno] = dictAlumnoEditar

def cargarAlumnos(strAlumnos):
    alumnos = []
    lstAlumnos = strAlumnos.splitlines()
    for l in lstAlumnos:
        alumnoData = l.split(',')
        dictAlumno = {
            'nombre':alumnoData[0],
            'email':alumnoData[1],
            'celular':alumnoData[2]
        }
        alumnos.append(dictAlumno)
    return alumnos

def grabarAlumnos(listaAlumnos):
    strAlumnos = ""

    for dictAlumno in listaAlumnos:
        for clave,valor in dictAlumno.items():
            strAlumnos += valor
            if clave != 'celular':
                strAlumnos += ','
            else:
                strAlumnos += '\n'
    return strAlumnos
######################################