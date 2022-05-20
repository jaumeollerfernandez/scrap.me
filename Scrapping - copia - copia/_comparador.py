#Realizar la clase comparador, el cual se le pasará el array obtenido con los precios actuales.
#Habrá dos métodos, el FicheroExiste() y el Comparación().
#FicheroExiste() deberá ver si se ha realizado el archivo o no. Si existe, leerá el archivo y lo guardará en un array
#Comparacion() deberá comparar los dos datos de los dos arrays. Leerá el anterior mediante el método, y luego lo comparará con el nuevo.
#Si no hay novedad, mantendrá los precios actualizados.
import _captadorDatosWeb as cp
import __TratoFicheros as tf
import _conexion as con
import datetime



class ComparadorFinal():
    def __init__(self, preciosactuales,user):
        self.preciosactuales = preciosactuales
        self.user=user
    
    def FicheroAlertaExiste(self):
        #Lo unico que hace este metodo es crear el archivo si no existe.
        try:
            #Si existe, lo abre por aquí.
            ale = open(f"DB/{self.user}_alertas.txt")
        except IOError:
            #Si no existe, lo crea y lo escribe.
            ale = open(f"DB/{self.user}_alertas.txt","w")
            print("Nuevo archivo de alertas creado")
        finally:
            ale.close()

    def datosDBExiste(self):
        
        con.Conexion("comparador").escritura(self.preciosactuales)
        
            
    def comparacion(self):
        
        self.datosDBExiste()
        response = con.Conexion("comparador").lectura(self.user)
        i=0
        while i < len(response):
            
            if response[i][0] == int(self.preciosactuales[i][0]):
                if response[i][3] > self.preciosactuales[i][3]:
                    con.Conexion("comparador").update(self.preciosactuales[i][3],self.preciosactuales[i][0],self.user)
                    print('precio cambiado')
            i+=1
        #Aquí leerá el archivo db con la clase escritura
        # oldfile = tf.TratoFicheros(fichero).lectura()
        # resultado = []
        # #Empieza las comparaciones y búsquedas de precios
        # for i in range(len(oldfile)):
        #     #Iteramos para buscar una coincidencia en el nombre
        #     x=oldfile[i][0]
        #     y=self.preciosactuales[i][0]
        #     if oldfile[i][0] == self.preciosactuales[i][0]:
        #         if oldfile[i][1] != self.preciosactuales[i][1]:
        #             oldfile[i][1]=self.preciosactuales[i][1]
        #             #Convertimos a decimal
        #         a = float(self.preciosactuales[i][2])
        #         b = float(oldfile[i][2])
        #             #Comparamos precios. Si es menor, lo machaca.
        #         if a < b:
        #             oldfile[i][2] = str(a)
        #                 #Realiza la alerta correspondiente y la escribe en el documento.
        #             self.FicheroAlertaExiste()
        #             time = str(datetime.datetime.now())
        #             with open ("DB/alertas.txt","a") as f:
        #                 f.write("El precio de ")
        #                 f.write(oldfile[i][1])
        #                 f.write(" es de ")
        #                 f.write(str(a))
        #                 f.write(" a las ")
        #                 f.write(time)
        #                 f.write("\n")
        # #Escribe los datos actualizados a la base de datos.                
        # tf.TratoFicheros("db.txt",oldfile).escritura()
        
        # return oldfile











# try:
#     f = open("filename.txt")
#     # Do something with the file
# except IOError:
#     f = open("Success.txt","w")

# finally:
#     f.close()












# try:
#     f = open("filename.txt")
#     # Do something with the file
# except IOError:
#     f = open("Success.txt","w")

# finally:
#     f.close()