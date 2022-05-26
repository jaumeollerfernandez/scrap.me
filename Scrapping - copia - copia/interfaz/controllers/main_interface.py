from datetime import time
import os
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from views.comparador_interface import MainWindowInterface
import _captadorDatosWeb as cdw
import __TratoFicheros as tf
import _comparador as cp
import _conexion as cn
# from alter_main_program import _comparador as compara
from time import sleep
from threading import Thread


class MainInterface(QWidget,MainWindowInterface):
    def __init__(self,user,widget):
        super().__init__()
        self.setupUi(self)
        self.user = user
        self.widget = widget

        #Hilos para ejecutar las funciones de scraping
        self.h1 = Thread(target=self.hilo_captador)

        # Cuadros de texto
        self.URLtext = self.URL
        self.PRICEtext = self.Precio
        self.ALERTtext = self.Alert
        self.PRODUCTtext = self.NombreProducto

        self.ValorTiempo = self.spinBox
        self.play_button.setDisabled(True)
        self.stop_button.setDisabled(True)
        self.sleep_button.clicked.connect(self.Definirtiempo)
        self.play_button.clicked.connect(self.h1.start)
        self.bol = False

        self.actionAbrir_alertas_txt.triggered.connect(self.deleteFile_alertas)
        self.actionAbrir_db_txt.triggered.connect(self.deleteFile_db)
        self.actionEliminar_alertas_txt.triggered.connect(self.deleteFile_alertas)
        self.actionEliminar_db_txt.triggered.connect(self.deleteFile_db)
    
    #Esta función elimina el hilo para volverlo a lanzar, y así liberar memoria
            
    def openfile_alertas(self):
        #No funciona bien, porque requiere ruta absoluta.
        os.startfile("C:/Users/jaume/Mi unidad/DAW/Github/scrap.me/scrapping_txt/alter_main_program/BD/alertas.txt")

    def openfile_db(self):
        os.startfile("alter_main_program/BD/db.txt")

    def deleteFile_alertas(self):
        fp = open("alter_main_program/BD/alertas.txt","a")
        fp.seek(0,0)
        fp.truncate()
        fp.close()

    def deleteFile_db(self):
        os.remove("alter_main_program/BD/db.txt")
      

    def deleteFile_urltag(self):
        fp = open("alter_main_program/BD/url_tag.txt","w")
        fp.seek(0,0)
        fp.truncate()
        fp.close()

    def Stop(self):
        self.bol = False
        while self.h1.is_alive():
            print("El Hilo esta Vivo")
            sleep(0.5)
        
        self.h1 = Thread(target=self.hilo_captador)
        self.play_button.clicked.connect(self.h1.start)
        self.play_button.setDisabled(True)
        self.stop_button.setDisabled(True)

    def hilo_captador(self):
        print("Inicio Hilo")
        self.bol = True
        self.stop_button.clicked.connect(self.Stop)
        while self.bol == True:
            self.PRODUCTtext.clear()
            self.PRICEtext.clear()
            self.URLtext.clear()
            self.ALERTtext.clear()
            m = cdw.CaptadorPrecios(self.user).getData()
            cp.ComparadorFinal(m,self.user).comparacion()
            datos = cn.Conexion('comparador').lectura(self.user)
            self.Meterdatosenpantalla(datos)
            sleep(self.ValorTiempo)
        print("Finaliza Hilo")
        self.stop_button.clicked.connect(self.Stop)
        self.sleep_button.clicked.connect(self.Definirtiempo)

    def Meterdatosenpantalla(self,array):
        i=0
        while i < len(array):
            self.PRODUCTtext.addItem(array[i][2])     
            self.PRICEtext.addItem(array[i][3])
            self.URLtext.addItem(array[i][4])
            i+=1
    
    def Meteralertasenpantalla(self,a):
        self.ALERTtext.addItem(str(a))
    
    def Definirtiempo(self):
        self.ValorTiempo = self.spinBox.value()
        self.play_button.setDisabled(False)
        self.stop_button.setDisabled(False)
        
    def cerrarbool(self):
        self.bol = False

    

