# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowsjugytE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import resource_rc


class start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.to_main_menu_func)
    
    def to_main_menu_func(self):
        self.cams = main_menu()
        self.cams.show()
        self.close() 
    
    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(857, 625)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 10, 141, 61))

        font = QFont()
        font.setPointSize(24)

        self.label.setFont(font)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 120, 431, 131))

        font1 = QFont()
        font1.setPointSize(20)
        font1.setKerning(True)

        self.label_2.setFont(font1)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(360, 530, 161, 31))

        font2 = QFont()
        font2.setPointSize(19)

        self.label_3.setFont(font2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 390, 211, 51))

        font3 = QFont()
        font3.setPointSize(15)
        self.pushButton.setFont(font3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-70, 220, 261, 381))
        self.label_4.setPixmap(QPixmap(u":/newPrefix/assets/1.png"))

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(540, 220, 301, 371))
        self.label_5.setPixmap(QPixmap(u":/newPrefix/assets/2.png"))

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")

        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0425\u041f\u0424\u041a \u041e\u041f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043b\u0456\u043a \u0437\u0430\u043c\u043e\u0432\u043b\u0435\u043d\u044c \u0430\u0442\u0435\u043b\u044c\u0454 \u0437 \u043f\u043e\u0448\u0438\u0442\u0442\u044f \u0442\u0430 \u0440\u0435\u043c\u043e\u043d\u0442\u0443 \u043e\u0434\u044f\u0433\u0443", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0435\u0440\u0441\u043e\u043d 2022", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u0434\u043e \u043c\u0435\u043d\u044e", None))
        self.label_4.setText("")
        self.label_5.setText("")


class main_menu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tostart.clicked.connect(self.tostartfunc)
        self.exit.clicked.connect(self.exitfunc)

    def exitfunc(self):
        print('exiting...')
        sys.exit()

    def tostartfunc(self):
        self.cams = start()
        self.cams.show()
        self.close() 

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(800, 522)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.clients = QPushButton(self.centralwidget)
        self.clients.setObjectName(u"clients")
        self.clients.setGeometry(QRect(50, 70, 131, 31))

        self.workers = QPushButton(self.centralwidget)
        self.workers.setObjectName(u"workers")
        self.workers.setGeometry(QRect(220, 70, 131, 31))

        self.zakazi = QPushButton(self.centralwidget)
        self.zakazi.setObjectName(u"zakazi")
        self.zakazi.setGeometry(QRect(390, 70, 131, 31))

        self.poslugi = QPushButton(self.centralwidget)
        self.poslugi.setObjectName(u"poslugi")
        self.poslugi.setGeometry(QRect(560, 70, 131, 31))

        self.tostart = QPushButton(self.centralwidget)
        self.tostart.setObjectName(u"tostart")
        self.tostart.setGeometry(QRect(280, 450, 191, 31))

        self.exit = QPushButton(self.centralwidget)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(710, 480, 75, 23))

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 270, 211, 131))
        self.label.setPixmap(QPixmap(u":/newPrefix/assets/4.png"))
        self.label.setScaledContents(True)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(470, 280, 241, 111))
        self.label_2.setPixmap(QPixmap(u":/newPrefix/assets/3.png"))
        self.label_2.setScaledContents(True)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.clients.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0456\u0454\u043d\u0442\u0438", None))
        self.workers.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0438", None))
        self.zakazi.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437\u0438", None))
        self.poslugi.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0443\u0433\u0438", None))
        self.tostart.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u0438\u0441\u044f \u043d\u0430 \u043f\u043e\u0447\u0430\u0442\u043a\u043e\u0432\u0438\u0439 \u0435\u043a\u0440\u0430\u043d", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0445\u0456\u0434", None))
        self.label.setText("")
        self.label_2.setText("")



if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = start()
    widget.show()
    

    try:
        sys.exit(app.exec_())
    except:
        print('exiting..')