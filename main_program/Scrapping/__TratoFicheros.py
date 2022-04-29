from fileinput import close
from msilib.schema import Class
from pickle import NONE


class TratoFicheros:
    def __init__(self,p1=NONE,p2=NONE):
        self.nombreFichero = p1
        self.p2 = p2
        
    
    def lectura(self):
        fp = open(self.nombreFichero,'r')
        datos = '.'
        lista=[]
        while datos != '':
            datos=fp.readline()
            if datos !='':
                datos=datos.rstrip('\n')
                dato = datos.split('*')
                lista.append(dato)
        fp.close()
        return lista
    
    
    
    def escritura(self):
        fp = open(self.nombreFichero,'w')
        i=0
        while i < len(self.p2):
            j=0
            while j < len(self.p2[i]):
                fp.write(self.p2[i][j])
                if j!=(len(self.p2[i])-1):
                    fp.write('*')
                j+=1
            fp.write('\n')
            i+=1
        fp.close()
        
# lista=[['www.amazon.com','<div>','<div2>'],['www.amazon2.com','<div>','<div2>']]       


# b = TratoFicheros(p1='archivo2.txt',p2=lista)
# a=b.lectura()
# print(len(a[0]))
# # b.escritura()