from datetime import time
import webbrowser
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
from testeo.comparador_interface import Ui_MainWindow
from alter_main_program import _captadorDatosWeb as cp
from alter_main_program import __TratoFicheros as tf
from alter_main_program import _comparador as compara
from time import sleep
from threading import Thread


class main_window(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Botones
        ButtonStop = self.stop_button
        ButtonPlay = self.play_button

        #Hilos para ejecutar las funciones de scraping
        self.h1 = Thread(target=self.hilo_captador)

        #Cuadros de texto
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
        # self.actionAbrir_alertas_txt
        # self.actionAbrir_db_txt
        self.actionAbrir_alertas_txt.triggered.connect(self.openfile_alertas)
        self.actionAbrir_db_txt.triggered.connect(self.openfile_db)
        self.actionEliminar_alertas_txt.triggered.connect(self.deleteFile_alertas)
        self.actionEliminar_db_txt.triggered.connect(self.deleteFile_db)
        
    #Esta función elimina el hilo para volverlo a lanzar, y así liberar memoria
    
    def openfile_alertas(self):
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
        # fp = open("alter_main_program/BD/db.txt","w")
        # fp.seek(0,0)
        # fp.truncate()
        # fp.close()

    def deleteFile_urltag(self):
        fp = open("alter_main_program/BD/url_tag.txt","w")
        fp.seek(0,0)
        fp.truncate()
        fp.close()

    def Stop(self):
        self.bol = False
        while self.h1.is_alive():
            print("esta vivo")
            sleep(0.5)
        
        self.h1 = Thread(target=self.hilo_captador)
        self.play_button.clicked.connect(self.h1.start)
        self.play_button.setDisabled(True)
        self.stop_button.setDisabled(True)

    def hilo_captador(self):
        print("inicia")
        self.bol = True
        self.stop_button.clicked.connect(self.Stop)
        while self.bol == True:
            self.PRODUCTtext.clear()
            self.PRICEtext.clear()
            self.URLtext.clear()
            self.ALERTtext.clear()
            m = cp.CaptadorPrecios('alter_main_program/BD/url_tag.txt',self.Meterdatosenpantalla, self).getData()
            compara.ComparadorFinal(m,self.Meteralertasenpantalla, self).comparacion("alter_main_program/BD/db.txt")
            sleep(self.ValorTiempo)
        print("finaliza")
        self.stop_button.clicked.connect(self.Stop)
        self.sleep_button.clicked.connect(self.Definirtiempo)

    def Meterdatosenpantalla(self,a,b,c):
        self.PRODUCTtext.addItem(str(a))     
        self.PRICEtext.addItem(str(b))
        self.URLtext.addItem(str(c))
    
    def Meteralertasenpantalla(self,a):
        self.ALERTtext.addItem(str(a))
        
    def Definirtiempo(self):
        self.ValorTiempo = self.spinBox.value()
        self.play_button.setDisabled(False)
        self.stop_button.setDisabled(False)



    
    

