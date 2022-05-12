#IMPORTACIÓN DE LIBRERIAS
import requests
from time import sleep
from bs4 import BeautifulSoup
from pickle import NONE
import alter_main_program.__TratoFicheros as tf
from testeo import main_window
#---------------------------------------------------------------------------------------------------------

#CLASE PARA BUSCAR LOS PRECIOS Y NOMBRES DE LAS WEBS SOLICITADAS
class CaptadorPrecios:
    def __init__(self,p1='BD/url_tag.txt', f=None,cv=None):
        self.data = p1
        self.b=tf.TratoFicheros(self.data,NONE).lectura()
        #self.PRUEBA = main_window.main_window()
        self.func = f
        self.v = cv
        self.headers = {
                'User-Agent': 'Mozilla/6.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
                'Accept-Language': 'en-US, en;q=0.5'
            }
      
   
#MÉTODO ESTÁTICO PARA CONSEGUIR EL PRECIO (RECORREMOS LOS TAGS DE LA LISTA QUE RECIBIMOS Y LOS USAMOS)
    @staticmethod
    def getPrice(soup,i,self):
        product_price=''
        results_prices = soup.find(self.b[i][2], {self.b[i][3]: self.b[i][4]})
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
        result_name = soup.find(self.b[i][5], {self.b[i][6]: self.b[i][7]})
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
            while j < len(lista[i][2]):
                if (ord(lista[i][2][j])>=48 and ord(lista[i][2][j])<=57 or lista[i][2][j]==',') and cont < 3:
                    if lista[i][2][j]==',':
                        condicion=True
                    if condicion:
                        cont+=1
                    precio+=lista[i][2][j]
                j+=1
            precio = self.standardPriceFloat(precio)
            lista[i][2]=precio
            i+=1
            
    
    
    
#METODO PARA EL REQUEST E INSTANCIACION DE METODOS PRECIO Y NOMBRE
    def getData(self):
        
        lista=[]
        i=0
        cont=0
        while i<len(self.b):
            sleep(1.5)
            cont+=1
            req = requests.get(self.b[i][1], headers=self.headers)
            
            print(req.status_code)
            soup = BeautifulSoup(req.content, 'html.parser')
            #############################################################################   
            product_price = self.getPrice(soup,i,self)
            #############################################################################
            product_name = self.getName(soup,i,self)        
            #############################################################################
            lista.append([str(cont),product_name,product_price,self.b[i][1]])
            #self.PRUEBA.Meterdatosenpantalla(product_name, product_price, self.b[i][1], 1)
            #self.func(product_name, product_price, self.b[i][1], 1)
            self.v.Meterdatosenpantalla(product_name, product_price, self.b[i][1], 1)

            product_price=''
            product_name=''
            
            i+=1
        self.standardPrice(self,lista)
        return lista
            
            
#DEVUELVE UNA LISTA(ARRAY) CON ID,NOMBRE,PRECIO,URL (DATOS ACTUALIZADOS)
