import os
import time
""" APLICACIÓN CRUD
C - CREATE
R - READ
U - UPDATE
D - DELETE
PARA ESTE CASO USAREMOS ALUMNOS
[
    {'nombre':'','email':'','celular':''},
    {'nombre':'','email':'','celular':''}
]
"""
alumnos = [
    {'nombre':'cesar mayta',
    'email':'cesarmayta@gmail.com',
    'celular':'956290589'}
    ]

opcion = 0
while(opcion != 5):
    if(opcion != 0):
        time.sleep(2)
        os.system("clear")
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
    """)
    opcion = int(input("INGRESE LA OPCIÓN A EJECUTAR : "))
    os.system("clear")
    if(opcion == 1):
        print(
        """
        ============================
        [1] REGISTRO DE NUEVO ALUMNO
        ============================
        """)
    elif(opcion == 2):
        print(
        """
        ========================
        [2]  LISTADO DE ALUMNOS
        ========================
        """)
    elif(opcion == 3):
        print(
        """
        ========================
        [3]  ACTUALIZAR UN ALUMNO
        ========================
        """)
    elif(opcion == 4):
        print(
        """
        ========================
        [4]  ELIMINAR ALUMNO
        ========================
        """)
    elif(opcion == 5):
        print(
        """
        ===========================
        EL SISTEMA SE ESTA CERRANDO
        ===========================
        """)
    else:
        print(
        """
        ===========================
            OPCIÓN INCORRECTA!!!
        ===========================
        """)
