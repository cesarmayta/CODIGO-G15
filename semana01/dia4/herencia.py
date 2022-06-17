class Persona:
    def __init__(self,nom,ema):
        self.nombre = nom
        self.email = ema

    def mostrar(self):
        print("Nombre : " + self.nombre)
        print("Email : " + self.email)

class Alumno(Persona):
    
    def __init__(self,nom,ema,nota):
        super().__init__(nom,ema)
        self.nota = nota
    
    def mostrar(self):
        super().mostrar()
        print("Nota : " + str(self.nota))

class Profesor(Persona):
    
    def __init__(self,nom,ema,esp):
        super().__init__(nom,ema)
        self.especialidad = esp
    
    def mostrar(self):
        super().mostrar()
        print('Especialidad : ' + self.especialidad)

alu1 = Alumno('Carlos tello','ctello@gmail.com',20)
alu1.mostrar()

profe1 = Profesor('Cesar Mayta','cesarmayta@gmail.com','backend')
profe1.mostrar()