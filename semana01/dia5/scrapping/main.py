import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioPromedio.aspx")


def scrapping_tipocambio():
    if(url.status_code == 200):
        print("pagina encontrada")
        #print(url.text)
        html = BeautifulSoup(url.text,'html.parser')
        tabla = html.find_all('table',{'id':'ctl00_cphContent_rgTipoCambio_ctl00'})
        #print(tabla)
        filaDolar = html.find_all('tr',{'id':'ctl00_cphContent_rgTipoCambio_ctl00__0'})
        #print(filaDolar)
        moneda = filaDolar[0].find('td',{'class':'APLI_fila3'})
        compra = filaDolar[0].find('td',{'class':'APLI_fila2'})
        venta = filaDolar[0].find('td',{'class':'APLI_fila2'}).findNext('td')
        print(moneda.get_text())
        print(compra.get_text())
        print(venta.get_text())

        cambio_valores = filaDolar[0].find_all('td',{'class':'APLI_fila2'})
        print(cambio_valores[0].get_text())
        print(cambio_valores[1].get_text())
    else:
        print("error " + str(url.status_code))

if __name__ == "__main__" :
    scrapping_tipocambio()