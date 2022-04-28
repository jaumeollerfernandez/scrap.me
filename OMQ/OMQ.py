#pip install pyzmq
import threading
from time import thread_time_ns
import zmq
from threading import Thread

class Comunicacion(threading.Thread):
    def __init__(self,type="SUB", host=None, function = None):
        threading.Thread.__init__ (self)
        self.__type = type
        self.__finish_thead = False
        if self.__type == "PUB":
            _zmq = zmq.PUB
        elif self.__type == "SUB":
            _zmq = zmq.SUB
        else:
            pass #error
        self.__context = zmq.Context()
        self.__socket = self.__context.socket(_zmq)
        self.__function = function
        if self.__type == "PUB":
            self.__socket.bind("tcp://127.0.0.1:2000")
        else:
            self.__socket.connect("tcp://127.0.0.1:2000")
            self.__socket.subscribe('')
            #self.__thread = Thread(target=self.__recibir_thread,args=(function,self.__socket))

    def run(self):
        self.__finish_thead = False
        while not self.__finish_thead:
            #print(zmq.NOBLOCK) #valor1
            message = None
            try:
                message = self.__socket.recv_json(flags = 1)
            except zmq.ZMQError as e:
                pass
            if message != None:
                self.__function(message)
                print(message)
        #print("saliendo")
        
        
    def stop(self):
        self.__finish_thead = True

    def enviar(self, datos):
        print("enviar datos json")
        self.__socket.send_json(datos)
        print("enviado ")


    def recibir(self):        
        message =  self.__socket.recv_json()
        self.__function(message)
        print(message)

    def cerrar(self):
        self.__socket.close()
        self.__context.term()
