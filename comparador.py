#Realizar la clase comparador, el cual se le pasará el array obtenido con los precios actuales.
#Habrá dos métodos, el FicheroExiste() y el Comparación().
#FicheroExiste() deberá ver si se ha realizado el archivo o no. Si existe, leerá el archivo y lo guardará en un array
#Comparacion() deberá comparar los dos datos de los dos arrays. Leerá el anterior mediante el método, y luego lo comparará con el nuevo.
#Si no hay novedad, mantendrá los precios actualizados.

import writethings


preciosactuales = ["Penetrator3000", "5,99","www.rabolargo.com/product/69"]

class ComparadorFinal():
    def __init__(self, preciosactuales):
        self.preciosactuales = preciosactuales

    def FicheroExiste(self):
        try:
            #Si existe, lo abre por aquí.
            f = open("db.csv")
        except IOError:
            #Si no existe, lo crea y lo escribe.
            f = open("db.csv","w")
            for i in range(len(self.preciosactuales)):
                #Reemplazar por la clase escritura.
                f.write(self.preciosactuales[i])
                f.write(";")
            print("Nuevo archivo creado")
        finally:
            f.close()
    def comparacion(self):
        #Aquí leerá el archivo db.csv con la clase escritura
        oldfile = writethings.escritura("db.csv").leer()
        print(oldfile)






ComparadorFinal(preciosactuales).comparacion()






# try:
#     f = open("filename.txt")
#     # Do something with the file
# except IOError:
#     f = open("Success.txt","w")

# finally:
#     f.close()