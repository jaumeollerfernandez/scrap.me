from bs4 import BeautifulSoup
import requests

def buscaweb(web):
    web = web
    file = requests.get(web).text
    webparsed = BeautifulSoup(file, "lxml")
    return webparsed

def tipo(url):

    tipo = []
    bool = False
    finish = False
    url_l = list(url)
    #Busca en la URL la etiqueta de la empresa que es
    for i in range(len(url_l)):
        if bool == True and url_l[i] != ".":
            tipo.append(url_l[i])
        elif url_l[i] == "." and bool == False and finish == False:
            bool = True
        elif url_l[i] == "." and bool == True:
            finish = True
            bool = False

    resultado = ("".join(tipo))
    #Buscamos en el csv la etiqueta de la empresa, para obtener los parámetros.
    db = open("empresas.csv","r")
    leer = "a"
    comparanombre = []
    finish = False
    while leer != "":
        leer = db.read(1)
        if leer != ";":
            comparanombre.append(leer)
        
        

    db.close()

print(tipo("https://www.elcorteingles.es/electronica/ordenadores/"))
    
