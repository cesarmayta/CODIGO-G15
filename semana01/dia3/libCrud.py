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

######################################