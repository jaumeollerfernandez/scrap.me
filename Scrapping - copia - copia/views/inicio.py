# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inicio.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
from assets import img_login

class MainInicio(object):
    def setupUi(self, inicio):
        if not inicio.objectName():
            inicio.setObjectName(u"inicio")
        inicio.resize(972, 533)
        self.entrada = QFrame(inicio)
        self.entrada.setObjectName(u"entrada")
        self.entrada.setGeometry(QRect(0, 0, 971, 531))
        self.entrada.setStyleSheet(u"background-color:white")
        self.entrada.setFrameShape(QFrame.StyledPanel)
        self.entrada.setFrameShadow(QFrame.Raised)
        self.groupBox_2 = QGroupBox(self.entrada)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(490, 0, 505, 541))
        self.groupBox_2.setStyleSheet(u"background-color: rgba(222,222,222,255);")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 100, 241, 181))
        self.label_2.setStyleSheet(u"image:url(:/imgLogin/883149-200.png);")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 30, 341, 51))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 300, 281, 31))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(70, 350, 351, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 410, 351, 51))
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(110, 480, 301, 20))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setUnderline(True)
        self.label_8.setFont(font3)
        self.groupBox = QGroupBox(self.entrada)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(-10, 0, 501, 541))
        self.groupBox.setStyleSheet(u"background-color: rgb(0,0,0);")
        self.ok = QPushButton(self.groupBox)
        self.ok.setObjectName(u"ok")
        self.ok.setGeometry(QRect(30, 320, 451, 30))
        font4 = QFont()
        font4.setBold(True)
        self.ok.setFont(font4)
        self.ok.setStyleSheet(u"QPushButton#ok{\n"
"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#ok:pressed{\n"
"background-color: rgb(230,230,230);\n"
"}")
        self.botonRegistro = QPushButton(self.groupBox)
        self.botonRegistro.setObjectName(u"botonRegistro")
        self.botonRegistro.setGeometry(QRect(120, 450, 291, 24))
        self.botonRegistro.setFont(font4)
        self.botonRegistro.setStyleSheet(u"QPushButton#botonRegistro{\n"
"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#botonRegistro:pressed{\n"
"background-color: rgb(230,230,230);\n"
"}")
        self.user_input = QLineEdit(self.groupBox)
        self.user_input.setObjectName(u"user_input")
        self.user_input.setGeometry(QRect(30, 220, 451, 40))
        self.user_input.setStyleSheet(u"background-color: rgba(47,49,52,200);\n"
"color: rgb(255,255,255);\n"
"border-radius: 2px;\n"
"padding-left: 10px;\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,255);\n"
"padding-bottom: 2px;")
        self.password_input = QLineEdit(self.groupBox)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(30, 270, 451, 40))
        self.password_input.setStyleSheet(u"background-color: rgba(47,49,52,200);\n"
"color: rgb(255,255,255);\n"
"border-radius: 2px;\n"
"padding-left: 10px;\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,255);\n"
"padding-bottom: 2px;")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(24, 60, 461, 141))
        font5 = QFont()
        font5.setFamilies([u"Bahnschrift"])
        font5.setPointSize(47)
        self.label.setFont(font5)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: rgb(255,255,255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 420, 151, 16))
        font6 = QFont()
        font6.setPointSize(11)
        self.label_3.setFont(font6)
        self.label_3.setStyleSheet(u"color: rgb(255,255,255);")

        self.retranslateUi(inicio)

        QMetaObject.connectSlotsByName(inicio)
    # setupUi

    def retranslateUi(self, inicio):
        inicio.setWindowTitle(QCoreApplication.translate("inicio", u"Form", None))
        self.groupBox_2.setTitle("")
        self.label_2.setText("")
        self.label_4.setText(QCoreApplication.translate("inicio", u"WEB SCRAPPING", None))
        self.label_5.setText(QCoreApplication.translate("inicio", u"\u00bfQue es el Web Scrapping?", None))
        self.label_6.setText(QCoreApplication.translate("inicio", u"Es una t\u00e9cnica utilizada para extraer informaci\u00f3n \n"
"de sitios web.", None))
        self.label_7.setText(QCoreApplication.translate("inicio", u"TIENDAS PARA PODER SCRAPPEAR:\n"
"Amazon, Kyoto Electrodom\u00e9sticos, Miro, Worten", None))
        self.label_8.setText(QCoreApplication.translate("inicio", u"Proyecto hecho por el grupo MPG de DAW 1", None))
        self.groupBox.setTitle("")
        self.ok.setText(QCoreApplication.translate("inicio", u"Iniciar Sesi\u00f3n", None))
        self.botonRegistro.setText(QCoreApplication.translate("inicio", u"Reg\u00edstrarse", None))
        self.user_input.setText("")
        self.user_input.setPlaceholderText(QCoreApplication.translate("inicio", u"Introduce Usuario...", None))
        self.password_input.setText("")
        self.password_input.setPlaceholderText(QCoreApplication.translate("inicio", u"Introduce Contrase\u00f1a...", None))
        self.label.setText(QCoreApplication.translate("inicio", u"INICIAR SESI\u00d3N", None))
        self.label_3.setText(QCoreApplication.translate("inicio", u"Crear nuevo usuario !!", None))
    # retranslateUi

