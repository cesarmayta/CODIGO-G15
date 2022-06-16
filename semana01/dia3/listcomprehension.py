listaNombre = []
strNombre = "cesar mayta"
for strLetra in strNombre:
    listaNombre.append(strLetra)

print(listaNombre)

listaNombre = [strLetra for strLetra in strNombre]
print(listaNombre)

listaNumeros = [num for num in range(101)]
print(listaNumeros)

print("=" *100)
listaMultiplosDeDos = []
for numero in range(101):
    if numero % 2 == 0:
        listaMultiplosDeDos.append(numero)

print(listaMultiplosDeDos)
print("usando list comprehension")
listaMultiplosDeDos = [numero for numero in listaNumeros if (numero % 2 == 0)]
print(listaMultiplosDeDos)
