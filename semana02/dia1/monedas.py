from flask import Flask,request
from TipoCambioSbs import TipoCambioSbs

app = Flask(__name__)



@app.route('/')
def index():
    estilo = '<style>'
    estilo += 'table,th,td { border : 1px solid; }'
    estilo += '</style>'
    tipocambio = TipoCambioSbs()
    resultado = estilo + '<center><h1>TIPOS DE CAMBIOS DEL DÍA - SBS</h1>'
    resultado += tipocambio.obtenerTipoCambio()
    resultado += '</center>'

    return resultado

app.run(debug=True)