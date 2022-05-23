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
        ButtonStop.clicked.connect(self.Stop)
        ButtonPlay.clicked.connect(self.h1.start)
        self.bol = False
        # self.actionAbrir_alertas_txt
        # self.actionAbrir_db_txt
        self.actionEliminar_alertas_txt.triggered.connect(self.deleteFile_alertas)
        self.actionEliminar_db_txt.triggered.connect(self.deleteFile_db)
        
    #Esta función elimina el hilo para volverlo a lanzar, y así liberar memoria
            
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

    def hilo_captador(self):
        # self.bol = True
        # while self.bol == True:
        #     # self.play_button.
        self.h1 = Thread(target=self.hilo_captador)
        m = cp.CaptadorPrecios('alter_main_program/BD/url_tag.txt',self.Meterdatosenpantalla, self).getData()
        compara.ComparadorFinal(m,self.Meteralertasenpantalla, self).comparacion("alter_main_program/BD/db.txt")
        
    def Meterdatosenpantalla(self,a,b,c):
        self.PRODUCTtext.addItem(str(a))     
        self.PRICEtext.addItem(str(b))
        self.URLtext.addItem(str(c))
    
    def Meteralertasenpantalla(self,a):
        self.ALERTtext.addItem(str(a))
    

