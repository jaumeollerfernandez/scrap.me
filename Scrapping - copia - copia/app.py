from curses import window
import sys
from PySide6.QtWidgets import QApplication
from PySide6 import QtWidgets
from interfaz.controllers.inicio import Inici
from interfaz.controllers.register import Register

if __name__=='__main__':
    app = QApplication()
    widget = QtWidgets.QStackedWidget()
    print(dir(widget))
    inicio = Inici(widget)
    register = Register(widget)
    widget.addWidget(inicio)
    widget.addWidget(register)
    
    
    print(widget.count())
    widget.setFixedWidth(944)
    widget.setFixedHeight(492)
    widget.setCurrentIndex(0)
    widget.show()
    sys.exit(app.exec()) 
    

