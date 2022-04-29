#https://doc.qt.io/qtforpython/PySide6/QtWidgets/index.html
#designer en:
#C:\Users\???\AppData\Local\Programs\Python\Python?????\Lib\site-packages\PySide6\designer.exe
#MAC
#/usr/local/Cellar/python@3.9/3.9.12/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pyside6 
# ejecutar el designer dentro del dir, preferencias ventana - ventana unica
# open -a designer.app 

#
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
from PySide6.QtCore import QEvent

#fin clases

#definición clases de forms QT/pyside
#Formulario principal carga del documento UI
class VentanaP(QObject):  # QMainWindow 
    def __init__(self, ui_file, parent=None):
        #llamada del constructor padre HERENCIA
        #super().__init__(parent)
               
        super(VentanaP, self).__init__(parent)
        #CARGA del DOCUMENTO UI gráfico y apertura
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        #carga del documento al atributo window
        loader = QUiLoader()
        self.window = loader.load(ui_file)

        ui_file.close()
        #definicion variable atributo y carga de objetos graficos para interactuar, 
        #se carga el nombre especificado en el designer
        self.list = self.window.findChild(QListWidget, 'listWidget')
        self.listh = self.window.findChild(QListWidget, 'listWidget_2')
        self.txt_line = self.window.findChild(QLineEdit, 'txt_line')
        self.btn = self.window.findChild(QPushButton, 'bt_enviar')
        self.label = self.window.findChild(QLabel, 'label')
        #asignamos la funcion para tratar acciones 
        self.btn.clicked.connect(self.__funcion)
    
        #fin carga de objetos
        #otros atributos
        self.contador = 0

        #---------------- 
        #propiedad para eventos
        #carga el event filter con la funcion eventFilter
        self.window.installEventFilter(self)
        # o cargar el parent para lanzar los eventos de la funcion
        #self.setParent(self.window)
        self.window.show()

    #funcion para asignar a un boton del formulario
    def __funcion(self):
        #self.sender() retorna el objeto y permite obtener propiedades del objeto
        print(self.sender().text())
        print("Este es tu texto escrito: "+ self.txt_line.text())
        self.contador+=1
        self.label.setText(str(self.contador))
        dlg = Dialog()
        dlg.exec()
    
    def actualiza(self,v):
        #accedemos a la list y agregamos un elemento
        self.list.addItem(str(v)); 

    def hilo_actualiza(self, datos):
        #obtiene un json de datos, filtra. Uno forma de ejecutar paralelismo
        self.listh.addItem(str(datos['message'])); 

    def closeEvent(self, e):
        print("?")
        QMainWindow.closeEvent(self, e)

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
            print("????SDSD")

#dialogo
class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.label = QLabel("label")
        layout = QVBoxLayout()
        self.setWindowTitle("Hi, soy un dialgo")
        self.label.setText("HOLA !!!")
        layout.addWidget(self.label)
        self.setLayout(layout)
        #tamaño fijo
        #self.setFixedSize(400, 200)
        self.resize(240, 120)


# funciona para cargar en un hilo y actualizar datos del formulario 
# se ejecuta en paralelo al gestor de ventanas
def hilo1 (form, otro=None):
    c = 0
    while True:
        time.sleep(5)
        form.actualiza(c)
        c+=1

    


#main 
if __name__ == "__main__":
    #inicio de la aplicacion grafica
    app = QApplication(sys.argv)
    #creacion de la instancia inicial de la ventana
    print(os.path.dirname(sys.argv[0] )+ '\\'+'ventanaP.ui')
    # os.getcwd() retorna el path de ejecucion, diferente al del sys
    form = VentanaP(os.path.dirname(sys.argv[0] )  + '\\'+'ventanaP.ui')
    #creacion de hilos, asignacion de funcion y parametros que tenga definida la funcion
    #hilo de actualizar cada 5 segundos el list
    h1 = Thread(target=hilo1,args=( form, "algo"))
    h1.start()
    #hilo de actualizar por proceso independiente 
    #creación del cliente de comunicacion
    c = Comunicacion(type = 'SUB',function= form.hilo_actualiza)
    c.start()
    #h2 = Thread(target=hilo2,args=( form, "algo"))
    #h2.start()
    sys.exit(app.exec())
