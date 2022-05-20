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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

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
        self.groupBox_2.setGeometry(QRect(480, 0, 501, 541))
        self.groupBox_2.setStyleSheet(u"background-color: rgb(222,222,222);")
        self.groupBox = QGroupBox(self.entrada)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(-20, 0, 501, 541))
        self.groupBox.setStyleSheet(u"background-color: rgb(0,0,0);")
        self.ok = QPushButton(self.groupBox)
        self.ok.setObjectName(u"ok")
        self.ok.setGeometry(QRect(200, 390, 75, 24))
        self.ok.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.botonRegistro = QPushButton(self.groupBox)
        self.botonRegistro.setObjectName(u"botonRegistro")
        self.botonRegistro.setGeometry(QRect(200, 480, 75, 24))
        self.botonRegistro.setStyleSheet(u"background-color: rgb(255,255,255);")
        self.user_input = QLineEdit(self.groupBox)
        self.user_input.setObjectName(u"user_input")
        self.user_input.setGeometry(QRect(60, 140, 401, 31))
        self.user_input.setStyleSheet(u"background-color: white;")
        self.password_input = QLineEdit(self.groupBox)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setGeometry(QRect(60, 200, 401, 31))
        self.password_input.setStyleSheet(u"background-color: white;")

        self.retranslateUi(inicio)

        QMetaObject.connectSlotsByName(inicio)
    # setupUi

    def retranslateUi(self, inicio):
        inicio.setWindowTitle(QCoreApplication.translate("inicio", u"Form", None))
        self.groupBox_2.setTitle("")
        self.groupBox.setTitle("")
        self.ok.setText(QCoreApplication.translate("inicio", u"LOGIN", None))
        self.botonRegistro.setText(QCoreApplication.translate("inicio", u"REGISTER", None))
        self.user_input.setText(QCoreApplication.translate("inicio", u"USUARIO", None))
        self.password_input.setText(QCoreApplication.translate("inicio", u"CONTRASE\u00d1A", None))
    # retranslateUi

