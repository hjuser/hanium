# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '1rpWMzK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(500, 350, 93, 28))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(600, 350, 93, 28))
        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(90, 220, 201, 22))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(90, 160, 201, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 190, 201, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 240, 201, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 100, 371, 251))
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(90, 280, 181, 19))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\uc785\ub825", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\ucde8\uc18c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ucc28\ub7c9\ubc88\ud638\uc785\ub825", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ucd9c\ucc28\uc608\uc815\uc2dc\uac04\uc785\ub825", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<\uc0ac\uc6a9\uc548\ub0b4>\n"
"\n"
" 1. \ucc28\ub7c9\ubc88\ud638\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694.\n"
" 2. \ucd9c\ucc28 \uc2dc\uac04\uc744 \uc801\uc5b4\uc8fc\uc138\uc694\n"
" (\uc815\ud655\ud558\uc9c0 \uc54a\ub2e4\uba74 \uc544\ub798 \ubc15\uc2a4\ub97c \uccb4\ud06c\ud574\uc8fc\uc138\uc694) \n"
" \ubaa8\ub450 \uc785\ub825\ud558\uc168\ub2e4\uba74 \uc785\ub825\ubc84\ud2bc\uc744 \ub20c\ub7ec \ub9c8\ubb34\ub9ac \ud574\uc8fc\uc138\uc694.", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\uc815\ud655\ud558\uc9c0 \uc54a\uc74c", None))
    # retranslateUi

