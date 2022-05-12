
from __TratoFicheros import TratoFicheros 

class Captador():
    def __init__(self, inicio):
        self.trat = TratoFicheros("alter_main_program/BD/baseDatos.txt")
        
        self.inicio = inicio

    def introducirURL(self, lista):
        # fin = "s"
        # while fin!="n":
        #     print("Introducir URL")
        #     url = input()
        #     lista.append(url)
        #     print("¿Desea introducir otra URL?")
        #     print("Pulse 's' para seguir o 'n' para finalizar")
        #     fin = input()
        #     if fin =='S':
        #         fin = 's'
        #     if fin == 'N':
        #         fin = 'n'
        #     if fin!='S' and fin!= 's' and fin!= 'N' and fin!= 'n':
        #         print("Por favor, intruduce 's' o 'n':")
        #         fin = input()
        listaEmpresa = self.extraerNombres(lista)
        self.setTags(self.trat,listaEmpresa, lista, listaURLTAGS)

    def extraerNombres(self, url):
        tipo = []
        listaEmpresa = []
        bool = False
        finish = False
        for i in range(len(url)): # recorro la lista de url
            string = str(url[i]) # convierto en string cada url para quedarme con el nombre
            for j in range(len(string)):
                if bool == True and string[j] != ".":
                    tipo.append(string[j])
                elif string[j] == "." and bool == False and finish == False:
                    bool = True
                elif string[j] == "." and bool == True:
                    finish = True
                    bool = False
            if j>len(tipo): # si ya tengo el nombre de la empresa
                resultado = ("".join(tipo))
                listaEmpresa.append(resultado)
                finish = False
                tipo = []

        return listaEmpresa # la función devuelve el array con los nombres de empresa

    def setTags(self, trat, listaEmpresa, lista, listaURLTAGS):
        ##############################################################
        # Pasar a lectura() el nombre del archivo de tags.
        # lectura() devuelve una lista de tags y nombres
        emprTags = trat.lectura() # Instancia TratoFichero.lectura()
        
        
        ##############################################################

        # Comparar empresa[] con el nombre de las empresas del archivo de tags
        
        listaURLTAGS = []
        i=0
        id=1
        while i < len(listaEmpresa): # lista2
            j=0
            while j < len(emprTags): # lista1
                if listaEmpresa[i]==emprTags[j][0]:
                    z=1
                    listaInterior=[]
                    cont=0
                    listaInterior.append(str(id))
                    while z < len(emprTags[i]):
                        cont+=1
                        if cont <2:
                            listaInterior.append(lista[i])
                        listaInterior.append(emprTags[j][z])
                        z+=1
                    listaURLTAGS.append(listaInterior)
                    id=id+1
                    j=len(emprTags[i])
                j+=1
            i+=1

        #print(listaURLTAGS) # devuelve una matriz de url y tags 
        # [ [1, 'www.youtube.com', '<div1>', '<div2.1>', '<div2.2>', '<div2.3>'], 
        #   [2, 'www.google.es', '<div3>', '<div4>'], 
        #   [3, 'www.kyoto.com', '<div5>', '<div6>'] ]
        TratoFicheros("BD/url_tag.txt", listaURLTAGS).escritura()



listaURLTAGS=[]
 # instancia de la clase
# Pasar a escritura el array con las url y sus tags
# TratoFicheros.escritura(listaEmpresa) # Instancia TratoFichero.escritura()
# tratList.escritura()



#################################################################
############ Funcionamiento de los métodos ######################
#################################################################
"""
introducirURL:
- El usuario ingresa las url a tratar

"""