from tabulate import tabulate
#import tabulate

table = [
    ["cesar mayta","cesarmayta@gmail.com","989989"],
    ["cesar mayta","cesarmayta@gmail.com","989989"]
]
columnas = ["nombre","email","celular"]
print(tabulate(table,headers=columnas,tablefmt="grid"))