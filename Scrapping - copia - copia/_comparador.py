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
            ale = open(f"BD/{self.user}_alertas.txt")
        except IOError:
            #Si no existe, lo crea y lo escribe.
            ale = open(f"BD/{self.user}_alertas.txt","w")
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
                    print('El Precio del Producto ha cambiado')
                    time = str(datetime.datetime.now())
                    with open (f"BD/{self.user}_alertas.txt","a") as f: 
                        f.write("El precio de ")
                        f.write(response[i][2])
                        f.write(" es de ")
                        f.write(str(self.preciosactuales[i][3]))
                        f.write(" a las ")
                        f.write(time)
                        f.write("\n")
            i+=1