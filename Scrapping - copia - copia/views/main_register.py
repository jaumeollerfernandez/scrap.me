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
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class RegisterForm(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1001, 477)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 0, 991, 481))
        self.frame.setStyleSheet(u"background-color:white")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.botonInicio = QPushButton(self.frame)
        self.botonInicio.setObjectName(u"botonInicio")
        self.botonInicio.setGeometry(QRect(130, 380, 191, 24))
        self.botonInicio.setStyleSheet(u"background-color:green")
        self.registro_boton = QPushButton(self.frame)
        self.registro_boton.setObjectName(u"registro_boton")
        self.registro_boton.setGeometry(QRect(650, 370, 201, 24))
        self.registro_boton.setStyleSheet(u"background-color:blue")
        self.nick_input = QLineEdit(self.frame)
        self.nick_input.setObjectName(u"nick_input")
        self.nick_input.setGeometry(QRect(630, 130, 201, 21))
        self.nick_input.setStyleSheet(u"margin: 2px;")
        self.nombre_input = QLineEdit(self.frame)
        self.nombre_input.setObjectName(u"nombre_input")
        self.nombre_input.setGeometry(QRect(630, 230, 201, 21))
        self.nombre_input.setStyleSheet(u"margin: 2px;")
        self.apellidos_input = QLineEdit(self.frame)
        self.apellidos_input.setObjectName(u"apellidos_input")
        self.apellidos_input.setGeometry(QRect(630, 280, 201, 21))
        self.apellidos_input.setStyleSheet(u"margin: 2px;")
        self.contrasea_input = QLineEdit(self.frame)
        self.contrasea_input.setObjectName(u"contrasea_input")
        self.contrasea_input.setGeometry(QRect(630, 180, 201, 21))
        self.contrasea_input.setStyleSheet(u"margin: 2px;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.botonInicio.setText(QCoreApplication.translate("Form", u"al login", None))
        self.registro_boton.setText(QCoreApplication.translate("Form", u"REGISTRAR", None))
    # retranslateUi

