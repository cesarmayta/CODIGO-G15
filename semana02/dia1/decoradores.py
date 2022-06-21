def decorador(func):
    def envoltura():
        print('esto se añade a la función principal')
        func()
    return envoltura

def mayusculas(func):
    def envolutora(texto):
        return func(texto).upper()
    return envolutora

@decorador
def mensaje():
    print('hola mundo')

#mensaje = decorador(mensaje)
mensaje()

@mayusculas
def mostrarTexto(texto):
    return  'texto : ' + texto

print(mostrarTexto('hola mundo'))