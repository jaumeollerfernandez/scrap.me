from bs4 import BeautifulSoup
import requests

def obtenwalapruebaCSV():
    #Esta sería la versión de prueba para testear con la web de wala
    resultado = ["localhost","span","class","base","price"]
    return resultado

def nombreyprecio(p1,p2,p3,p4):
    #Pasándole los parámetros de la lista de cada empresa, obtiene el nombre y precio
    nombre = textside.find(p1, {p2:p3}).text
    precio = textside.find(p1, {p2:p4}).text
    escribe_enCSV(nombre,precio)
    return nombre,precio

def escribe_enCSV(nombre,precio):
    f = open("precios.csv", "w")
    f.write(nombre)
    f.write(";")
    f.write(precio)
    f.write(";")
    f.write("\n")
    f.close()


html_request = requests.get("http://localhost:81/index_.php").text

textside = BeautifulSoup(html_request,"lxml")

csv = obtenwalapruebaCSV()
precios = nombreyprecio("span","class","base","price-wrapper")

print(precios)
