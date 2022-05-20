from curses import window
import sys
from PySide6.QtWidgets import QApplication
from interfaz.controllers.main_window import MainWindowForm

if __name__=='__main__':
    app = QApplication()
    
    window = MainWindowForm()
    window.show()
    
    sys.exit(app.exec()) 