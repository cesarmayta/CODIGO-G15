"""
EJERCICIOS 01:
INGRESE UN TEXTO Y UN DIVISOR Y LUEGO MUESTRE EL MISMO TEXTO PERO DIVIDO POR EL DIVISOR
EJEMPLO:
INGRESO 
TEXTO = ABCDEFG
DIVISOR = 2
RESULTADO:
AB
CD
EF
G
"""
#ENTRADA
texto = input("ingrese el texto : ")
divisor = int(input("ingrese divisor: "))
longitudTexto = len(texto)
print("la longitud del texto que ingresaste es : " + str(longitudTexto))
#PROCESO
#texto[0:2]
#text[2:4]
#for contador in range(0,len(texto),divisor):
    #SALIDA
 #   print(texto[contador:divisor+contador])
 #texto = ['A','B','C','D','E','F','G']

#texto[0:2]
#text[2:4]
#texto[4:6]
for contador in range(0,longitudTexto,divisor):
    salida = texto[contador:divisor+contador]
    print(salida)