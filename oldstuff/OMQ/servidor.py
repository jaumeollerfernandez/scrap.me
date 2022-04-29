from OMQ import Comunicacion
import time

try:
    c = Comunicacion(type = 'PUB')
    print("envio")
    time.sleep(10)
    c.enviar({"message": "soy un mensaje del servidor - 1"})
    input()
    c.enviar({"message": "soy un mensaje del servidor - 2"})
    input()
except Exception as e:
    print(e)
    input()