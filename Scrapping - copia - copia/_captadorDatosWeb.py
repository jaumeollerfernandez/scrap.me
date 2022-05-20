#IMPORTACIÓN DE LIBRERIAS
import requests
from time import sleep
from bs4 import BeautifulSoup
from pickle import NONE
import __TratoFicheros as tf
import _conexion as cn
import _Captador as cp
#---------------------------------------------------------------------------------------------------------

#CLASE PARA BUSCAR LOS PRECIOS Y NOMBRES DE LAS WEBS SOLICITADAS
class CaptadorPrecios:
    
    def __init__(self,user=''):
        self.user = user
        self.b=cn.Conexion('').lectura_TAGS_relacion_User(self.user)
        print(self.b)
        self.headers = {
                'User-Agent': 'Mozilla/6.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
                'Accept-Language': 'en-US, en;q=0.5'
            }
      
   
#MÉTODO ESTÁTICO PARA CONSEGUIR EL PRECIO (RECORREMOS LOS TAGS DE LA LISTA QUE RECIBIMOS Y LOS USAMOS)
    @staticmethod
    def getPrice(soup,i,self):
        product_price=''
        results_prices = soup.find(self.b[i][3], {self.b[i][4]: self.b[i][5]})
        y = results_prices    
        try:
            if len(results_prices.findChildren())>0:
                try:
                    for result in results_prices.findChildren():
                        product_price += result.text
                        product_price += ','
                except:
                    pass
            else:
                product_price = results_prices.text
        except:
            pass  
        return product_price
    
    
#MÉTODO ESTÁTICO PARA CONSEGUIR EL NOMBRE OFICIAL (RECORREMOS LOS TAGS DE LA LISTA QUE RECIBIMOS Y LOS USAMOS)   
    @staticmethod
    def getName(soup,i,self):
        product_name=''
        result_name = soup.find(self.b[i][6], {self.b[i][7]: self.b[i][8]})
        x=  result_name 
        try:
            if len(result_name.findChildren())>0:
                try:
                    for result in result_name.findChildren():
                        product_name += result.text
                except:
                    pass
            else:
                product_name = result_name.text
        except:
            pass  
        return product_name
    
#METODO PARA ESTANDARIZAR LOS PRECIOS PARTE-2  (AL FINALIZAR LA PARTE-1 RECLAMA ESTA) 
    @staticmethod
    def standardPriceFloat(string):
        string=list(string)
        i=0
        while i < len(string):
            if string[i]==',':
                string[i]='.'
                i=len(string)
            i+=1
        return "".join(string)
    
    
#METODO PARA ESTANDARIZAR LOS PRECIOS PARTE-1  
    @staticmethod
    def standardPrice(self,lista):
        i=0
        while i < len(lista):
            j=0
            condicion=False
            coma=0
            cont=0
            precio=''
            while j < len(lista[i][3]):
                if (ord(lista[i][3][j])>=48 and ord(lista[i][3][j])<=57 or lista[i][3][j]==',') and cont < 3:
                    if lista[i][3][j]==',':
                        condicion=True
                    if condicion:
                        cont+=1
                    precio+=lista[i][3][j]
                j+=1
            precio = self.standardPriceFloat(precio)
            lista[i][3]=precio
            i+=1
            
    
    
    
#METODO PARA EL REQUEST E INSTANCIACION DE METODOS PRECIO Y NOMBRE
    def getData(self):
        
        lista=[]
        i=0
        cont=0
        while i<len(self.b):
            sleep(1.5)
            cont+=1
            req = requests.get(self.b[i][2], headers=self.headers)
            
            print(req.status_code)
            soup = BeautifulSoup(req.content, 'html.parser')
            #############################################################################   
            product_price = self.getPrice(soup,i,self)
            #############################################################################
            product_name = self.getName(soup,i,self)        
            #############################################################################
            lista.append([self.b[i][0],self.user,product_name,product_price,self.b[i][2]])
            product_price=''
            product_name=''
            
            i+=1
        self.standardPrice(self,lista)
        print(lista)
        return lista
            
            
#DEVUELVE UNA LISTA(ARRAY) CON ID,NOMBRE,PRECIO,URL (DATOS ACTUALIZADOS)

# CaptadorPrecios()