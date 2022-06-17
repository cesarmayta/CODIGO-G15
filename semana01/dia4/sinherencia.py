class Alumno:
    
    def __init__(self,nom,ema,nota):
        self.nombre = nom
        self.email = ema
        self.nota = nota

    def mostrar(self):
        print("Nombre : " + self.nombre)
        print("Email : " + self.email)
        print("Nota : " + str(self.nota))

class Profesor:
    def __init__(self,nom,ema,esp):
        self.nombre = nom
        self.email = ema
        self.especialidad = esp
    
    def mostrar(self):
        print("Nombre : " + self.nombre)
        print("Email : " + self.email)
        print("Especialidad : " + self.especialidad )

alumnoCesar = Alumno('cesar mayta','cesarmayta@gmail.com',18)
alumnoCesar.mostrar()

alumnoNuevo = Alumno('Jorge Perez','jorge@gmail.com',20)
alumnoNuevo.mostrar()

nuevoProfesor = Profesor('Aldo Maretegui','aldito@gmail.com','backend')
nuevoProfesor.mostrar()