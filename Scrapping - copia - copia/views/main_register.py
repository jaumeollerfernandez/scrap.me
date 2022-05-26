# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registro.ui'
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

class RegisterForm(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(971, 531)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 981, 531))
        self.frame.setStyleSheet(u"background-color:white")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(470, -10, 501, 541))
        self.groupBox.setStyleSheet(u"background-color: rgb(0,0,0);")
        self.botonInicio = QPushButton(self.groupBox)
        self.botonInicio.setObjectName(u"botonInicio")
        self.botonInicio.setGeometry(QRect(110, 480, 291, 24))
        font = QFont()
        font.setBold(True)
        self.botonInicio.setFont(font)
        self.botonInicio.setStyleSheet(u"QPushButton#botonInicio{\n"
"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#botonInicio:pressed{\n"
"background-color: rgb(230,230,230);\n"
"}")
        self.nick_input = QLineEdit(self.groupBox)
        self.nick_input.setObjectName(u"nick_input")
        self.nick_input.setGeometry(QRect(30, 180, 451, 40))
        self.nick_input.setStyleSheet(u"background-color: rgba(47,49,52,200);\n"
"color: rgb(255,255,255);\n"
"border-radius: 2px;\n"
"padding-left: 10px;\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,255);\n"
"padding-bottom: 2px;")
        self.nombre_input = QLineEdit(self.groupBox)
        self.nombre_input.setObjectName(u"nombre_input")
        self.nombre_input.setGeometry(QRect(30, 280, 451, 40))
        self.nombre_input.setStyleSheet(u"background-color: rgba(47,49,52,200);\n"
"color: rgb(255,255,255);\n"
"border-radius: 2px;\n"
"padding-left: 10px;\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,255);\n"
"padding-bottom: 2px;")
        self.contrasea_input = QLineEdit(self.groupBox)
        self.contrasea_input.setObjectName(u"contrasea_input")
        self.contrasea_input.setGeometry(QRect(30, 230, 451, 40))
        self.contrasea_input.setStyleSheet(u"background-color: rgba(47,49,52,200);\n"
"color: rgb(255,255,255);\n"
"border-radius: 2px;\n"
"padding-left: 10px;\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,255);\n"
"padding-bottom: 2px;")
        self.contrasea_input.setEchoMode(QLineEdit.Password)
        self.apellidos_input = QLineEdit(self.groupBox)
        self.apellidos_input.setObjectName(u"apellidos_input")
        self.apellidos_input.setGeometry(QRect(30, 330, 451, 40))
        self.apellidos_input.setStyleSheet(u"background-color: rgba(47,49,52,200);\n"
"color: rgb(255,255,255);\n"
"border-radius: 2px;\n"
"padding-left: 10px;\n"
"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,255);\n"
"padding-bottom: 2px;")
        self.registro_boton = QPushButton(self.groupBox)
        self.registro_boton.setObjectName(u"registro_boton")
        self.registro_boton.setGeometry(QRect(30, 390, 451, 30))
        self.registro_boton.setFont(font)
        self.registro_boton.setStyleSheet(u"QPushButton#registro_boton{\n"
"background-color: rgb(255,255,255);\n"
"color: rgb(0,0,0);\n"
"border-radius: 5px;\n"
"}\n"
"QPushButton#registro_boton:pressed{\n"
"background-color: rgb(230,230,230);\n"
"}")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 461, 141))
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift"])
        font1.setPointSize(47)
        self.label.setFont(font1)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: rgb(255,255,255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 450, 201, 20))
        font2 = QFont()
        font2.setPointSize(11)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(255,255,255);")
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(-30, 0, 505, 541))
        self.groupBox_2.setStyleSheet(u"background-color: rgba(222,222,222,255);")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(116, 480, 301, 20))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setUnderline(True)
        self.label_8.setFont(font3)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(146, 20, 241, 61))
        font4 = QFont()
        font4.setPointSize(25)
        font4.setBold(True)
        self.label_2.setFont(font4)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(56, 140, 421, 51))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(False)
        self.label_7.setFont(font5)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(116, 90, 301, 51))
        font6 = QFont()
        font6.setPointSize(16)
        font6.setBold(True)
        self.label_9.setFont(font6)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(116, 210, 301, 51))
        self.label_10.setFont(font6)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(56, 260, 421, 51))
        self.label_11.setFont(font5)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(116, 330, 301, 51))
        self.label_12.setFont(font6)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(56, 380, 421, 51))
        self.label_13.setFont(font5)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(70, 76, 401, 4))
        self.line.setStyleSheet(u"background-color: black;\n"
"border-radius: 6px;\n"
"border-color: black;\n"
"border-width: 5px;")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle("")
        self.botonInicio.setText(QCoreApplication.translate("Form", u"Iniciar Ses\u00edon", None))
        self.nick_input.setPlaceholderText(QCoreApplication.translate("Form", u"Introduce Usuario...", None))
        self.nombre_input.setPlaceholderText(QCoreApplication.translate("Form", u"Introduce Nombre...", None))
        self.contrasea_input.setPlaceholderText(QCoreApplication.translate("Form", u"Introduce Contrase\u00f1a...", None))
        self.apellidos_input.setPlaceholderText(QCoreApplication.translate("Form", u"Introduce Apellidos...", None))
        self.registro_boton.setText(QCoreApplication.translate("Form", u"Reg\u00edstrate Ahora", None))
        self.label.setText(QCoreApplication.translate("Form", u"REGISTRATE", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u00bfYa tienes una cuenta?", None))
        self.groupBox_2.setTitle("")
        self.label_8.setText(QCoreApplication.translate("Form", u"Proyecto hecho por el grupo MPG de DAW 1", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"INFORMACI\u00d3N", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u00a1Gracias a este programa podr\u00e1s comprobar si los \n"
"productos que est\u00e1s buscando bajan o suben de precio!!", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u00bfPorque deber\u00eda registrarme?", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u00bfEs gratuito?", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Si!!, es un proyecto hecho para clase, no hay \n"
"nada que pagar!!", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u00bfHacer esto es legal?", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Solo ser\u00e1 legal si procede de fuentes de acceso p\u00fablico, \n"
"como este programa es para productos, es 100% legal!!", None))
    # retranslateUi

