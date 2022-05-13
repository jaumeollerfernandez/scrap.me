from datetime import time
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


class main_window(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Botones
        ButtonStop = self.stop_button
        ButtonPlay = self.play_button

        #Cuadros de texto
        self.URLtext = self.URL
        self.PRICEtext = self.Precio
        self.ALERTtext = self.Alert
        self.PRODUCTtext = self.NombreProducto
        ButtonStop.clicked.connect(self.say_hello)
        ButtonPlay.clicked.connect(self.Start)
    
    def say_hello(self):
        text = "aaaaaa"
        print(text)

    def Start(self):
        
        m = cp.CaptadorPrecios('alter_main_program/BD/url_tag.txt',self.Meterdatosenpantalla, self).getData()
        compara.ComparadorFinal.comparacion('alter_main_program/BD/db.txt',self.Meteralertasenpantalla, self)
    
    def Meterdatosenpantalla(self,a,b,c):
        self.PRODUCTtext.addItem(str(a))     
        self.PRICEtext.addItem(str(b))
        self.URLtext.addItem(str(c))
        #self.ALERTtext.addItem(str(d))
    
    def Meteralertasenpantalla(self,a):
        self.ALERTtext.addItem(str(a))

