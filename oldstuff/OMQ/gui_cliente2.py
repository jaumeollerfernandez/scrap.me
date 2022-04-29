#https://doc.qt.io/qtforpython/PySide6/QtWidgets/index.html
#designer en:
#C:\Users\???\AppData\Local\Programs\Python\Python?????\Lib\site-packages\PySide6\designer.exe
#MAC
#/usr/local/Cellar/python@3.9/3.9.12/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pyside6 
# ejecutar el designer dentro del dir, preferencias ventana - ventana unica
# open -a designer.app 

import sys
import os
#libreria de hilos
from threading import Thread
import time

#clase creada para la comunicación
from OMQ import Comunicacion

#clases para QT cada calse és un objeto necesario (se puede no importar las clases e importar toda la libreria)
from PySide6.QtUiTools import QUiLoader
#importar cada widget (objeto grafico) que haga falta o importar todo
from PySide6.QtWidgets import QVBoxLayout, QApplication, QPushButton, QLineEdit, QDialog, QLabel, QListWidget ,QMainWindow
from PySide6.QtCore import QFile, QIODevice, QObject
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QCloseEvent
from PySide6.QtCore import QEvent, QCoreApplication

#clase generada con la orden, genera un python con UI
#pyside6-uic ventanaP.ui -o ventanaP.py
from ventanaP import Ui_MainWindow
#*************************************************
#fin clases

#definición clases de forms QT/pyside
#Formulario principal carga la clase exportada del ui
class VentanaP(QMainWindow, Ui_MainWindow):  
    def __init__(self, parent=None):
        #llamada del constructor padre HERENCIA
        #super().__init__(parent)
        QMainWindow.__init__(self,parent)  

        self.setupUi(self)
        #definicion variable atributo y carga de objetos graficos para interactuar, 
        #se carga el nombre especificado en el designer
        #nombres de las variables que tenemos en la clase
        #listWidget
        #listWidget_2
        #txt_line
        #bt_enviar
        #label       
        #asignamos la funcion para tratar acciones 
        self.bt_enviar.clicked.connect(self.__funcion)
    
        #fin carga de objetos
        #otros atributos
        self.contador = 0
        self.hilo = True
        #----------------
        #propiedad para eventos
        #carga el event filter con la funcion eventFilter
        #self.window.installEventFilter(self)      
        self.show()
        #creacion de hilos, asignacion de funcion y parametros que tenga definida la funcion
        #hilo de actualizar por proceso independiente 
        #creación del cliente de comunicacion
        self.c = Comunicacion(type = 'SUB',function= self.hilo_actualiza)
        self.c.start()
        #gestion del hilo principal para actualizar el listview
        #hilo de actualizar cada 5 segundos el list
        h1 = Thread(target=self.__hilo1,args=( self, "algo"))
        h1.start()

    #funcion para asignar a un boton del formulario
    def __funcion(self):
        #self.sender() retorna el objeto y permite obtener propiedades del objeto
        print(self.sender().text())
        print("Este es tu texto escrito: "+ self.txt_line.text())
        self.contador+=1
        self.label.setText(str(self.contador))
        #abrir dialogo
        dlg = Dialog()
        dlg.exec()
    
    def actualiza(self,v):
        #accedemos a la list y agregamos un elemento
        self.listWidget.addItem(str(v)); 

    def hilo_actualiza(self, datos):
        #obtiene un json de datos, filtra. Uno forma de ejecutar paralelismo
        self.listWidget_2.addItem(str(datos['message'])); 

    def closeEvent(self, e):
        print("Cerrando la ventada")
        self.hilo = False
        self.c.stop()
        self.close

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Close:
            print("EVENTO LANZADO CLOSE")

    # funciona para cargar en un hilo y actualizar datos del formulario 
    # se ejecuta en paralelo al gestor de ventanas
    def __hilo1 (self, form, otro=None):
        c = 0
        while self.hilo:
            time.sleep(5)
            form.actualiza(c)
            c+=1

 #dialogo
class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.label = QLabel("label")
        #crear un layout para color elementos, tipo QVBoxLayout
        layout = QVBoxLayout()
        self.setWindowTitle("Hi, soy un dialgo")
        #creamos un objeto
        self.label.setText("HOLA !!!")
        #agregamos al layout
        layout.addWidget(self.label)
        #definimos el layout del dialog
        self.setLayout(layout)
        #tamaño fijo
        #self.setFixedSize(400, 200)
        self.resize(240, 120)

#main 
if __name__ == "__main__":
    #inicio de la aplicacion grafica
    app = QApplication(sys.argv)
    #creacion de la instancia inicial de la ventana
    #print(os.path.dirname(os.path.dirname(sys.argv[0] )  + '\\'+'ventanaP.ui')
    # os.getcwd() retorna el path de ejecucion, diferente al del sys
    form = VentanaP()

    sys.exit(app.exec())
