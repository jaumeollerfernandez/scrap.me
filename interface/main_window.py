from interface.comparador_interface import Ui_MainWindow
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from interface.comparador_interface import Ui_MainWindow

class main_window(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Botones
        ButtonStop = self.stop_button
        ButtonPlay = self.play_button

        #Cuadros de texto
        URLtext = self.URL
        PRICEtext = self.Precio
        ALERTtext = self.Alert
        PRODUCTtext = self.NombreProducto
        
    
    def say_hello(self):
        print("holaaaa")



        

