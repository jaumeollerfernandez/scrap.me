from curses import window
import sys
from PySide6.QtWidgets import QApplication
from interface.main_window import main_window

if __name__=='__main__':
    app = QApplication()
    
    window = main_window()
    window.show()
    
    sys.exit(app.exec()) 