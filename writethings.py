preciosactuales = ["Penetrator3000", "5,99","www.rabolargo.com/product/69"]

class escritura():
    def __init__(self, archivo):
        self.archivo = archivo
    
    def leer(self):
        f = open(self.archivo,"r")
        leer = "s"
        array = []
        arraycasifinal = []
        arrayfinal = []
        while leer != "":
            leer = f.read(1)
            if leer == "":
                break
            while leer != ";":
                array.append(leer)
                leer = f.read(1)
            arraycasifinal.append("".join(array))
            array = []
            arrayfinal.append(arraycasifinal)
        f.close()
        return arrayfinal

    def escribir(array, file):
        f = open(file, "w")
        for i in range(len(array)):
            f.write(array[i])
            f.write(";")
        f.close()
        print("Archivo escrito")

