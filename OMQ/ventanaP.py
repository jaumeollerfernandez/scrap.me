# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaP.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(527, 361)
        self.actionOtra_opci_n = QAction(MainWindow)
        self.actionOtra_opci_n.setObjectName(u"actionOtra_opci_n")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.bt_enviar = QPushButton(self.centralwidget)
        self.bt_enviar.setObjectName(u"bt_enviar")
        self.bt_enviar.setGeometry(QRect(280, 270, 81, 24))
        self.txt_line = QLineEdit(self.centralwidget)
        self.txt_line.setObjectName(u"txt_line")
        self.txt_line.setGeometry(QRect(20, 270, 251, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 300, 251, 16))
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 30, 211, 192))
        self.listWidget_2 = QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(280, 30, 211, 192))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 121, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 10, 221, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 527, 22))
        self.menuSoy_un_Men = QMenu(self.menubar)
        self.menuSoy_un_Men.setObjectName(u"menuSoy_un_Men")
        self.menuSub_Men = QMenu(self.menuSoy_un_Men)
        self.menuSub_Men.setObjectName(u"menuSub_Men")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSoy_un_Men.menuAction())
        self.menuSoy_un_Men.addAction(self.menuSub_Men.menuAction())
        self.menuSoy_un_Men.addSeparator()
        self.menuSub_Men.addAction(self.actionOtra_opci_n)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOtra_opci_n.setText(QCoreApplication.translate("MainWindow", u"Otra opci\u00f3n", None))
        self.bt_enviar.setText(QCoreApplication.translate("MainWindow", u"Pulsa boton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"contador", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"autoincremental", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"incremental proceso independiente", None))
        self.menuSoy_un_Men.setTitle(QCoreApplication.translate("MainWindow", u"Soy un Men\u00fa", None))
        self.menuSub_Men.setTitle(QCoreApplication.translate("MainWindow", u"Sub Men\u00fa", None))
    # retranslateUi

