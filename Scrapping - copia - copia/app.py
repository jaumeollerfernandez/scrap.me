from curses import window
import sys
from PySide6.QtWidgets import QApplication
from PySide6 import QtWidgets, QtGui
from interfaz.controllers.inicio import Inici
from interfaz.controllers.register import Register
import interfaz.controllers.main_interface as ci
import ctypes

if __name__=='__main__':
    app = QApplication()
    widget = QtWidgets.QStackedWidget()
    myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    widget.setWindowTitle("WEB SCRAPPING - M04 MPG")
    widget.setWindowIcon(QtGui.QIcon('assets/883149-200.png'))

    # print(dir(widget))
    
    inicio = Inici(widget)
    register = Register(widget)
    widget.addWidget(inicio)
    widget.addWidget(register)
    
    # print(widget.count())
    
    widget.setFixedWidth(971)
    widget.setFixedHeight(531)
    widget.setCurrentIndex(0)
    widget.show()
    app.exec()  
      
    sys.exit() 
    

