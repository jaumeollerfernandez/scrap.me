#Realizar la clase comparador, el cual se le pasará el array obtenido con los precios actuales.
#Habrá dos métodos, el FicheroExiste() y el Comparación().
#FicheroExiste() deberá ver si se ha realizado el archivo o no. Si existe, leerá el archivo y lo guardará en un array
#Comparacion() deberá comparar los dos datos de los dos arrays. Leerá el anterior mediante el método, y luego lo comparará con el nuevo.
#Si no hay novedad, mantendrá los precios actualizados.

import TratoFicheros
import datetime


m = [
    ["Penetrator3000", "2.99","www.rabolargo.com/product/69"],
    ["Penetrator4000","4.99","www.rabolargo.com/product/79"],
    ["Penetrator5000","8.99","www.rabolargo.com/product/60"]
    ]

class ComparadorFinal():
    def __init__(self, preciosactuales):
        self.preciosactuales = preciosactuales
    
    def FicheroAlertaExiste(self):
        #Lo unico que hace este metodo es crear el archivo si no existe.
        try:
            #Si existe, lo abre por aquí.
            ale = open("alertas.txt")
        except IOError:
            #Si no existe, lo crea y lo escribe.
            ale = open("alertas.txt","w")
            print("Nuevo archivo de alertas creado")
        finally:
            ale.close()

    def FicheroDBExiste(self):
        try:
            #Si existe, lo abre por aquí.
            f = open("db.txt")
        except IOError:
            #Si no existe, lo crea y lo escribe.
            f = open("db.txt","w")
            for i in range(len(self.preciosactuales)):
                #Reemplazar por la clase escritura.
                f.write(self.preciosactuales[i])
                f.write("*")
            print("Nuevo archivo creado")
        finally:
            f.close()
    def comparacion(self,fichero):
        #Aquí leerá el archivo db con la clase escritura
        oldfile = TratoFicheros.TratoFicheros(fichero).lectura()
        resultado = []
        #Empieza las comparaciones y búsquedas de precios
        for i in range(len(oldfile)):
            #Iteramos para buscar una coincidencia en el nombre
            for j in range(len(oldfile[0])):
                if oldfile[j][0] == self.preciosactuales[i][0]:
                    #Convertimos a decimal
                    a = float(self.preciosactuales[i][1])
                    b = float(oldfile[j][1])
                    #Comparamos precios. Si es menor, lo machaca.
                    if a < b:
                        oldfile[j][1] = str(a)
                        #Realiza la alerta correspondiente y la escribe en el documento.
                        self.FicheroAlertaExiste()
                        time = str(datetime.datetime.now())
                        with open ("alertas.txt","w") as f:
                            f.write("El precio de ")
                            f.write(oldfile[j][0])
                            f.write(" es de ")
                            f.write(str(a))
                            f.write(" a las ")
                            f.write(time)
                            f.write("\n")
        #Escribe los datos actualizados a la base de datos.                
        TratoFicheros.TratoFicheros("db.txt",oldfile).escritura()
        
        return oldfile


ComparadorFinal(m).comparacion("db.txt")













# try:
#     f = open("filename.txt")
#     # Do something with the file
# except IOError:
#     f = open("Success.txt","w")

# finally:
#     f.close()