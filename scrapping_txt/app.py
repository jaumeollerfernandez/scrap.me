from curses import window
import sys
from PySide6.QtWidgets import QApplication
from testeo.main_window import main_window

if __name__=='__main__':
    app = QApplication()
    
    window = main_window()
    window.show()
    app.exec()
    window.cerramosprograma()
    sys.exit()