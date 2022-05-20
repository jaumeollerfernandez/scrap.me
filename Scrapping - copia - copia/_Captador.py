import _conexion as cn


class Captador():
    def __init__(self,user):
        
        self.user=user
        

   

    def extraerNombres(self, url):
        empresa= ''
        condicion=False
        cont=0
        i=0
        while i < len(url):
            if url[i] == '.' and cont ==0:
                condicion = True
                cont+=1
                i+=1
            elif condicion and url[i]!='.' and cont==1:
                empresa+=url[i]
                i+=1
            elif condicion and url[i] == '.' and cont==1:
                i=len(url)
            else:
                i+=1
        return empresa 
            
        # tipo = []
        # listaEmpresa = []
        # bool = False
        # finish = False
        # for i in range(len(url)): # recorro la lista de url
        #     string = str(url[i]) # convierto en string cada url para quedarme con el nombre
        #     for j in range(len(string)):
        #         if bool == True and string[j] != ".":
        #             tipo.append(string[j])
        #         elif string[j] == "." and bool == False and finish == False:
        #             bool = True
        #         elif string[j] == "." and bool == True:
        #             finish = True
        #             bool = False
        #     if j>len(tipo): # si ya tengo el nombre de la empresa
        #         resultado = ("".join(tipo))
        #         listaEmpresa.append(resultado)
        #         finish = False
        #         tipo = []

        # return listaEmpresa # la función devuelve el array con los nombres de empresa

    def setTags(self,url):
        # listaURLS = []
        id=0
        urls=cn.Conexion('productos').lectura(self.user)
        i=0
        while i < len(urls):
            if urls[i][2] == url:
                id=urls[i][0]
            i+=1
        listaEmpresas = self.extraerNombres(url)
        cn.Conexion('url_tags').escritura_URL_TAGS(listaEmpresas,self.user,id)


listaURLTAGS=[]
 # instancia de la clase
# Pasar a escritura el array con las url y sus tags
# TratoFicheros.escritura(listaEmpresa) # Instancia TratoFichero.escritura()
# tratList.escritura()


# cn.Conexion('null').lectura_TAGS_relacion_User(listaEmpresas,self.user)
#################################################################
############ Funcionamiento de los métodos ######################
#################################################################
"""
introducirURL:
- El usuario ingresa las url a tratar

"""