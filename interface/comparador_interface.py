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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTimeEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(788, 460)
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
        self.NombreProducto = QPlainTextEdit(self.centralwidget)
        self.NombreProducto.setObjectName(u"NombreProducto")
        self.NombreProducto.setGeometry(QRect(10, 50, 171, 321))
        self.Alert = QPlainTextEdit(self.centralwidget)
        self.Alert.setObjectName(u"Alert")
        self.Alert.setGeometry(QRect(510, 50, 261, 321))
        self.Precio = QPlainTextEdit(self.centralwidget)
        self.Precio.setObjectName(u"Precio")
        self.Precio.setGeometry(QRect(190, 50, 91, 321))
        self.URL = QPlainTextEdit(self.centralwidget)
        self.URL.setObjectName(u"URL")
        self.URL.setGeometry(QRect(290, 50, 211, 321))
        self.stop_button = QPushButton(self.centralwidget)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setGeometry(QRect(710, 390, 61, 23))
        self.play_button = QPushButton(self.centralwidget)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setGeometry(QRect(630, 390, 75, 23))
        self.sleepTime = QTimeEdit(self.centralwidget)
        self.sleepTime.setObjectName(u"sleepTime")
        self.sleepTime.setGeometry(QRect(90, 390, 118, 22))
        self.nameTemporizador = QLabel(self.centralwidget)
        self.nameTemporizador.setObjectName(u"nameTemporizador")
        self.nameTemporizador.setGeometry(QRect(10, 390, 71, 16))
        self.sleep_button = QPushButton(self.centralwidget)
        self.sleep_button.setObjectName(u"sleep_button")
        self.sleep_button.setGeometry(QRect(230, 390, 75, 23))
        self.producto_name = QGroupBox(self.centralwidget)
        self.producto_name.setObjectName(u"producto_name")
        self.producto_name.setGeometry(QRect(50, 20, 61, 16))
        self.precio_name = QGroupBox(self.centralwidget)
        self.precio_name.setObjectName(u"precio_name")
        self.precio_name.setGeometry(QRect(200, 20, 81, 31))
        self.url_name = QGroupBox(self.centralwidget)
        self.url_name.setObjectName(u"url_name")
        self.url_name.setGeometry(QRect(380, 20, 31, 16))
        self.alerta_name = QGroupBox(self.centralwidget)
        self.alerta_name.setObjectName(u"alerta_name")
        self.alerta_name.setGeometry(QRect(620, 20, 61, 16))
        #MainWindow.setCentralwidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 788, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        # MainWindow.setMenuBar(self.menubar)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"scrap.me", None))
        self.actionAbrir_db_txt.setText(QCoreApplication.translate("MainWindow", u"Abrir db.txt", None))
        self.actionAbrir_alertas_txt.setText(QCoreApplication.translate("MainWindow", u"Abrir alertas.txt", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionEliminar_db_txt.setText(QCoreApplication.translate("MainWindow", u"Eliminar db.txt", None))
        self.actionEliminar_alertas_txt.setText(QCoreApplication.translate("MainWindow", u"Eliminar alertas.txt", None))
        self.NombreProducto.setPlainText("")
        self.Alert.setPlainText("")
        self.Precio.setPlainText("")
        self.URL.setPlainText("")
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.play_button.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.nameTemporizador.setText(QCoreApplication.translate("MainWindow", u"Temporizador", None))
        self.sleep_button.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.producto_name.setTitle(QCoreApplication.translate("MainWindow", u"Producto", None))
        self.precio_name.setTitle(QCoreApplication.translate("MainWindow", u"Precio", None))
        self.url_name.setTitle(QCoreApplication.translate("MainWindow", u"URL", None))
        self.alerta_name.setTitle(QCoreApplication.translate("MainWindow", u"Alerta", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

