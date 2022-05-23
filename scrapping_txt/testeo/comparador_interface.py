# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comparador_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(944, 492)
        MainWindow.setStyleSheet(u"")
        self.actionAbrir_db_txt = QAction(MainWindow)
        self.actionAbrir_db_txt.setObjectName(u"actionAbrir_db_txt")
        self.actionAbrir_alertas_txt = QAction(MainWindow)
        self.actionAbrir_alertas_txt.setObjectName(u"actionAbrir_alertas_txt")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionEliminar_db_txt = QAction(MainWindow)
        self.actionEliminar_db_txt.setObjectName(u"actionEliminar_db_txt")
        self.actionEliminar_alertas_txt = QAction(MainWindow)
        self.actionEliminar_alertas_txt.setObjectName(u"actionEliminar_alertas_txt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stop_button = QPushButton(self.centralwidget)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setGeometry(QRect(870, 420, 61, 23))
        self.play_button = QPushButton(self.centralwidget)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setGeometry(QRect(790, 420, 75, 23))
        self.sleep_button = QPushButton(self.centralwidget)
        self.sleep_button.setObjectName(u"sleep_button")
        self.sleep_button.setGeometry(QRect(24, 420, 101, 23))
        self.producto_name = QGroupBox(self.centralwidget)
        self.producto_name.setObjectName(u"producto_name")
        self.producto_name.setGeometry(QRect(50, 30, 61, 16))
        self.precio_name = QGroupBox(self.centralwidget)
        self.precio_name.setObjectName(u"precio_name")
        self.precio_name.setGeometry(QRect(310, 30, 81, 31))
        self.url_name = QGroupBox(self.centralwidget)
        self.url_name.setObjectName(u"url_name")
        self.url_name.setGeometry(QRect(550, 30, 31, 16))
        self.alerta_name = QGroupBox(self.centralwidget)
        self.alerta_name.setObjectName(u"alerta_name")
        self.alerta_name.setGeometry(QRect(800, 30, 61, 16))
        self.NombreProducto = QListWidget(self.centralwidget)
        self.NombreProducto.setObjectName(u"NombreProducto")
        self.NombreProducto.setGeometry(QRect(20, 50, 191, 351))
        self.Precio = QListWidget(self.centralwidget)
        self.Precio.setObjectName(u"Precio")
        self.Precio.setGeometry(QRect(230, 50, 211, 351))
        self.URL = QListWidget(self.centralwidget)
        self.URL.setObjectName(u"URL")
        self.URL.setGeometry(QRect(470, 50, 231, 351))
        self.Alert = QListWidget(self.centralwidget)
        self.Alert.setObjectName(u"Alert")
        self.Alert.setGeometry(QRect(730, 50, 201, 351))
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(140, 420, 131, 22))
        #MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        #MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 944, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        #MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir_db_txt)
        self.menuArchivo.addAction(self.actionAbrir_alertas_txt)
        self.menuArchivo.addAction(self.actionEliminar_db_txt)
        self.menuArchivo.addAction(self.actionEliminar_alertas_txt)
        self.menuArchivo.addAction(self.actionSalir)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir_db_txt.setText(QCoreApplication.translate("MainWindow", u"Abrir db.txt", None))
        self.actionAbrir_alertas_txt.setText(QCoreApplication.translate("MainWindow", u"Abrir alertas.txt", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionEliminar_db_txt.setText(QCoreApplication.translate("MainWindow", u"Eliminar db.txt", None))
        self.actionEliminar_alertas_txt.setText(QCoreApplication.translate("MainWindow", u"Eliminar alertas.txt", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.play_button.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.sleep_button.setText(QCoreApplication.translate("MainWindow", u"Tiempo (minutos)", None))
        self.producto_name.setTitle(QCoreApplication.translate("MainWindow", u"Producto", None))
        self.precio_name.setTitle(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.url_name.setTitle(QCoreApplication.translate("MainWindow", u"URL", None))
        self.alerta_name.setTitle(QCoreApplication.translate("MainWindow", u"Alerta", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

