capitales = {
    'Perú':'Lima',
    'Ecuador':'Quito',
    'Chile':'Santiago',
    'Uruguay':'Montevideo'
}

print(capitales)
nuevaCapital = {'Brasil':'Brasilia'}
capitales.update(nuevaCapital)
print(capitales)
capitales.update({'Ecuador':'Guayaquil'})
print(capitales.get('Ecuador'))

pais = input("Ingrese el pais:")
capital = capitales.get(pais,'no existe')
print("la capital de  " + pais + " es " + capital)

c = capitales.pop('Chile','no existe')
print("eliminaste " + c)
print(capitales)
