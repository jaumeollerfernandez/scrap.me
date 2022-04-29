from OMQ import Comunicacion
import time 
def a(j):
    print("impresion desde ", j)

c = Comunicacion(type = 'SUB',function= a)

print("esperando envio")
c.start()
#c.recibir(a)
i = 0
while i < 10:
    time.sleep(5)
    print(i)
    i+=1
c.stop() 

input()

