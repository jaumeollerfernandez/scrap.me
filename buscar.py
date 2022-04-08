from bs4 import BeautifulSoup
import requests


def webparsed(web):
    web = web
    file = requests.get(web).text
    webparsed = BeautifulSoup(file, "lxml")
    return webparsed


def obtenwalapruebaCSV():
    #Esta sería la versión de prueba para testear con la web de wala
    resultado = ["localhost",""]

def obtenParametrosCSV(url):

    tipo = []
    bool = False
    finish = False
    url_l = list(url)
    # Busca en la URL la etiqueta de la empresa que es
    for i in range(len(url_l)):
        if bool == True and url_l[i] != ".":
            tipo.append(url_l[i])
        elif url_l[i] == "." and bool == False and finish == False:
            bool = True
        elif url_l[i] == "." and bool == True:
            finish = True
            bool = False

    resultado = ("".join(tipo))
    # Buscamos en el csv la etiqueta de la empresa, para obtener los parámetros.
    db = open("empresas.csv", "r")
    leer = "a"
    resultado = []
    miniresultado = []
    finish = False
    cont = 0
    #Recorremos CSV para obtener los parámetros que necesitamos en una matriz.
    while leer != "":
        nombre = []
        #Aquí se obtiene el nombre
        while leer != ";" and cont == 0:
            leer = db.read(1)
            if leer != ";":
                nombre.append(leer)
            elif leer == ";":
                miniresultado.append("".join(nombre))
                nombre = []
        #Aquí se obtiene el primer parámetro
        cont += 1
        leer = "a"
        while leer != ";" and cont == 1:
            leer = db.read(1)
            if leer != ";":
                nombre.append(leer)
            elif leer == ";":
                miniresultado.append("".join(nombre))
                nombre = []
        leer = "a"
        cont += 1
        #Aquí se obtiene el segundo parámetro
        while leer != ";" and cont == 2:
            leer = db.read(1)
            if leer != ";":
                nombre.append(leer)
            elif leer == ";":
                miniresultado.append("".join(nombre))

        if leer == ";":
            leer = db.read(1)
        cont = 0
        #Aquí lo une a la matriz general, y reseteamos.
        resultado.append(miniresultado)
        miniresultado = []

    db.close()
    return resultado

