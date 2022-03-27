# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowsjugytE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PyQt5.QtSql     import QSqlDatabase, QSqlQuery, QSqlTableModel 
from PyQt5.QtCore import Qt
from PyQt5 import QtSql
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import resource_rc              # импорт ресурсов --- создается с помощью  ----  pyrcc5 resources.qrc -o resource_rc.py
import sqlite3                  
from PySide2.QtCore import Qt 


# Global exit func

def exitfunc():
    print('exiting...')
    sys.exit()


# Стартовое меню
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
        self.setWindowTitle('Стартове меню')
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
        
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0425\u041f\u0424\u041a \u041e\u041f", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043b\u0456\u043a \u0437\u0430\u043c\u043e\u0432\u043b\u0435\u043d\u044c \u0430\u0442\u0435\u043b\u044c\u0454 \u0437 \u043f\u043e\u0448\u0438\u0442\u0442\u044f \u0442\u0430 \u0440\u0435\u043c\u043e\u043d\u0442\u0443 \u043e\u0434\u044f\u0433\u0443", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0435\u0440\u0441\u043e\u043d 2022", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u0434\u043e \u043c\u0435\u043d\u044e", None))

        self.label_4.setText("")
        self.label_5.setText("")



# Главное меню
class main_menu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tostart.clicked.connect(self.tostartfunc)
        self.exit.clicked.connect(exitfunc)
        self.clients.clicked.connect(self.toclientsfunc)

    def toclientsfunc(self):
        self.cams = clients()
        self.cams.show()
        self.close()

    def tostartfunc(self):
        self.cams = start()
        self.cams.show()
        self.close() 

    def setupUi(self, MainWindow):
        self.setWindowTitle('Головне меню')

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
        
        self.clients.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0456\u0454\u043d\u0442\u0438", None))
        self.workers.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0438", None))
        self.zakazi.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437\u0438", None))
        self.poslugi.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0443\u0433\u0438", None))
        self.tostart.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u0438\u0441\u044f \u043d\u0430 \u043f\u043e\u0447\u0430\u0442\u043a\u043e\u0432\u0438\u0439 \u0435\u043a\u0440\u0430\u043d", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0445\u0456\u0434", None))
        self.label.setText("")
        self.label_2.setText("")




# Меню клиентов

class clients(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.to_main_menu_func)
        self.exit.clicked.connect(exitfunc)

        self.add_new_client.clicked.connect(self.to_add_clientfunc)
        self.view_clients.clicked.connect(self.to_clients_listfunc)

    def to_clients_listfunc(self):
        self.cams = clients_list()
        self.cams.show()
        self.close()

    def to_add_clientfunc(self):
        self.cams = add_client()
        self.cams.show()
        self.close() 

    def to_main_menu_func(self):
        self.cams = main_menu()
        self.cams.show()
        self.close() 

    def setupUi(self, MainWindow):
        self.setWindowTitle('Меню Клієнти')

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(832, 300)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.add_new_client = QPushButton(self.centralwidget)
        self.add_new_client.setObjectName(u"add_new_client")
        self.add_new_client.setGeometry(QRect(60, 140, 161, 31))
        self.view_clients = QPushButton(self.centralwidget)
        self.view_clients.setObjectName(u"view_clients")
        self.view_clients.setGeometry(QRect(330, 140, 161, 31))

        self.clients_zvit = QPushButton(self.centralwidget)
        self.clients_zvit.setObjectName(u"clients_zvit")
        self.clients_zvit.setGeometry(QRect(620, 140, 161, 31))

        self.back = QPushButton(self.centralwidget)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(0, 0, 41, 31))

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back.setIcon(icon)
        self.back.setIconSize(QSize(25, 25))
        self.back.setCheckable(False)
        self.back.setFlat(False)

        self.exit = QPushButton(self.centralwidget)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(790, 0, 41, 31))

        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit.setIcon(icon1)
        self.exit.setIconSize(QSize(25, 25))
        self.exit.setCheckable(False)
        self.exit.setFlat(False)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.add_new_client.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043d\u043e\u0432\u043e\u0433\u043e \u043a\u043b\u0456\u0454\u043d\u0442\u0430", None))
        self.view_clients.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0433\u043b\u044f\u0434 \u043a\u043b\u0456\u0454\u043d\u0442\u0456\u0432", None))
        self.clients_zvit.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0432\u0456\u0442\u043d\u0456\u0441\u0442\u044c \u043f\u043e \u043a\u043b\u0456\u0454\u0442\u0430\u043c", None))
        self.back.setText("")
        self.exit.setText("")
    # retranslateUi


class add_client(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.to_clients)
        self.exit.clicked.connect(exitfunc)
        self.submit_addittion.clicked.connect(self.addclient)

    def addclient(self):
        conn = sqlite3.connect("atelie.db") 
        name = self.name.text()
        phone = self.phone.text()

        try:
            with conn:
                row = (name, phone)
                # print('DATA =', row)      # for debugging

                query = '''insert into Клієнти (ПІБ, Телефон)
                        values (?, ?);'''
                conn.execute(query, row)

                self.name.clear()
                self.phone.clear()

                msg = QMessageBox()
                msg.setWindowTitle("Результат виконання")
                msg.setText("Операція виконана успішно!")
                x = msg.exec_() 

        except sqlite3.Error as e:
            # print(e)              for debugging
            # print(e.args)

            self.name.clear()
            self.phone.clear()

            msg = QMessageBox()
            msg.setWindowTitle("Результат виконання")
            msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
            x = msg.exec_() 

        conn.commit()
        conn.close()
        
    def to_clients(self):
        self.cams = clients()
        self.cams.show()
        self.close()  

    def setupUi(self, MainWindow):

        self.setWindowTitle('Додати клієнта')

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(569, 372)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.name = QLineEdit(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(190, 130, 261, 41))

        font = QFont()
        font.setPointSize(12)
        self.name.setFont(font)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 140, 161, 31))

        font1 = QFont()
        font1.setPointSize(11)

        self.label.setFont(font1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 190, 161, 31))
        self.label_2.setFont(font1)

        self.phone = QLineEdit(self.centralwidget)
        self.phone.setObjectName(u"phone")
        self.phone.setGeometry(QRect(190, 190, 261, 31))
        self.phone.setFont(font)

        self.submit_addittion = QPushButton(self.centralwidget)
        self.submit_addittion.setObjectName(u"submit_addittion")
        self.submit_addittion.setGeometry(QRect(350, 250, 101, 31))
        self.submit_addittion.setFont(font1)

        self.back = QPushButton(self.centralwidget)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(0, 0, 41, 31))

        font2 = QFont()
        font2.setPointSize(2)

        self.back.setFont(font2)

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back.setIcon(icon)
        self.back.setIconSize(QSize(25, 25))

        self.exit = QPushButton(self.centralwidget)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(530, 0, 41, 31))
        self.exit.setFont(font2)

        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit.setIcon(icon1)
        self.exit.setIconSize(QSize(25, 25))

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u041f\u0406\u0411 \u043a\u043b\u0456\u0454\u043d\u0442\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u043d\u043e\u043c\u0435\u0440 \u043a\u043b\u0456\u0454\u043d\u0442\u0430", None))
        self.submit_addittion.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438", None))
        self.back.setText("")
        self.exit.setText("")
    # retranslateUi


class clients_list(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.to_clients)
        self.exit.clicked.connect(exitfunc)
        self.downbutton.clicked.connect(self.next_item)
        self.upbutton.clicked.connect(self.previous_item)

    def next_item(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow()+1)
        
    def previous_item(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow()-1)

    def to_clients(self):
        self.cams = clients()
        self.cams.show()
        self.close()  

    def load_data(self):
        
        connection = sqlite3.connect("atelie.db")
        cur = connection.cursor()
        sqlquery = "SELECT * FROM Клієнти"
        tablerow = 0
        total_rows_count = 0

        for row in cur.execute(sqlquery):
            total_rows_count += 1

        self.tableWidget.setRowCount(total_rows_count)

        for row in cur.execute(sqlquery):

                    # print(row)        for debugging
            self.tableWidget.setItem(tablerow,0,QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow,1,QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow,2,QTableWidgetItem(row[2]))
            tablerow += 1


    def setupUi(self, MainWindow):
        
        self.setWindowTitle('Список клієнтів')

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(806, 445)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(80, 50, 671, 291))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnWidth(0,80)
        self.tableWidget.setColumnWidth(1,319)
        self.tableWidget.setColumnWidth(2,270)
        self.tableWidget.setHorizontalHeaderLabels(["Код клієнта","ПІБ","Телефон"])
        self.tableWidget.verticalHeader().setVisible(False)

        self.load_data()

        self.back = QPushButton(self.centralwidget)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(0, 0, 41, 31))

        font = QFont()
        font.setPointSize(2)

        self.back.setFont(font)

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back.setIcon(icon)
        self.back.setIconSize(QSize(25, 25))

        self.exit = QPushButton(self.centralwidget)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(760, 0, 41, 31))
        self.exit.setFont(font)

        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit.setIcon(icon1)
        self.exit.setIconSize(QSize(25, 25))

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 10, 101, 31))

        font1 = QFont()
        font1.setPointSize(17)

        self.label.setFont(font1)

        self.upbutton = QPushButton(self.centralwidget)
        self.upbutton.setObjectName(u"upbutton")
        self.upbutton.setGeometry(QRect(10, 150, 41, 41))

        font2 = QFont()
        font2.setPointSize(13)

        self.upbutton.setFont(font2)

        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/assets/up_arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.upbutton.setIcon(icon2)
        self.upbutton.setIconSize(QSize(30, 30))

        self.downbutton = QPushButton(self.centralwidget)
        self.downbutton.setObjectName(u"downbutton")
        self.downbutton.setGeometry(QRect(10, 190, 41, 41))

        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/assets/down_arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.downbutton.setIcon(icon3)
        self.downbutton.setIconSize(QSize(30, 30))

        self.find_edit = QLineEdit(self.centralwidget)
        self.find_edit.setObjectName(u"find_edit")
        self.find_edit.setGeometry(QRect(160, 350, 71, 21))

        font3 = QFont()
        font3.setPointSize(10)

        self.find_edit.setFont(font3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 350, 111, 21))
        self.label_2.setFont(font2)

        self.findbutton = QPushButton(self.centralwidget)
        self.findbutton.setObjectName(u"findbutton")
        self.findbutton.setGeometry(QRect(160, 380, 71, 31))
        self.findbutton.setFont(font2)

        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.back.setText("")
        self.exit.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0456\u0454\u043d\u0442\u0438", None))
        self.upbutton.setText("")
        self.downbutton.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u043a\u043b\u0456\u0454\u043d\u0442\u0430", None))
        self.findbutton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0448\u0443\u043a", None))
    # retranslateUi


if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = start()
    widget.show()
    

    try:
        sys.exit(app.exec_())
    except:
        print('exiting..')