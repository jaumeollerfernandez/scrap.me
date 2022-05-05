# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QScrollBar,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Main_window(object):
    def setupUi(self, Main_window):
        if not Main_window.objectName():
            Main_window.setObjectName(u"Main_window")
        Main_window.resize(944, 492)
        self.verticalLayout = QVBoxLayout(Main_window)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centra_widget = QFrame(Main_window)
        self.centra_widget.setObjectName(u"centra_widget")
        self.centra_widget.setFrameShape(QFrame.StyledPanel)
        self.centra_widget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.centra_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.background_frame = QFrame(self.centra_widget)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: rgb(255,246,244)")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.content_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 380, 111, 16))
        self.verticalScrollBar = QScrollBar(self.content_frame)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(870, 50, 16, 301))
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.insert_btn = QPushButton(self.content_frame)
        self.insert_btn.setObjectName(u"insert_btn")
        self.insert_btn.setGeometry(QRect(580, 400, 101, 41))
        self.insert_btn.setStyleSheet(u"background-color:rgb(62,108,255);\n"
"color:white")
        self.start_btn = QPushButton(self.content_frame)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setGeometry(QRect(760, 380, 111, 71))
        self.start_btn.setStyleSheet(u"background-color:rgb(79,236,112)\n"
"")
        self.input_url = QLineEdit(self.content_frame)
        self.input_url.setObjectName(u"input_url")
        self.input_url.setGeometry(QRect(30, 400, 551, 41))
        self.input_url.setStyleSheet(u"background-color:white")
        self.url_list = QListWidget(self.content_frame)
        self.url_list.setObjectName(u"url_list")
        self.url_list.setGeometry(QRect(40, 50, 831, 301))
        self.url_list.setStyleSheet(u"background-color:white\n"
"")

        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.centra_widget)


        self.retranslateUi(Main_window)

        QMetaObject.connectSlotsByName(Main_window)
    # setupUi

    def retranslateUi(self, Main_window):
        Main_window.setWindowTitle(QCoreApplication.translate("Main_window", u"Form", None))
        self.label.setText(QCoreApplication.translate("Main_window", u"INTRODUZCA URL:", None))
        self.insert_btn.setText(QCoreApplication.translate("Main_window", u"INSERT", None))
        self.start_btn.setText(QCoreApplication.translate("Main_window", u"START", None))
    # retranslateUi

