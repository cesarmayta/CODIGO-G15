import os
alumnos = []

if(os.path.isfile('alumnos.csv')):
    archivoAlumnos = open('alumnos.csv','r')
else:
    archivoAlumnos = open('alumnos.csv','w')
    archivoAlumnos.write('cesar mayta,cesarmayta@gmail.com,990909090')
    archivoAlumnos.write('\nana lopez,ana@gmail.com,9092332')
    archivoAlumnos.write('\njorge perez,jorge@gmail.com,90809890')

strAlumnos = archivoAlumnos.read()
print("paso1 capturamos todo el texto del archivo :\n " + strAlumnos)
archivoAlumnos.close()

lstAlumnos = strAlumnos.splitlines()
print(lstAlumnos)
for l in lstAlumnos:
    alumnoData = l.split(',')
    dictAlumno = {
        'nombre':alumnoData[0],
        'email':alumnoData[1],
        'celular':alumnoData[2]
    }
    alumnos.append(dictAlumno)

print(alumnos)

