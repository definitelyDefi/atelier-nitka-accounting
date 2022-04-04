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
import re


# Global exit func

def exit_func():
    print('exiting...')
    sys.exit()


# Стартовое меню
class start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.to_menu_button.clicked.connect(self.to_main_menu_func)
        self.setWindowIcon(QIcon(u":/newPrefix/assets/start_menu_icon.png"))

    def to_main_menu_func(self):
        self.cams = main_menu()
        self.cams.show()
        self.close() 
    
    def setupUi(self, MainWindow):

        from PyQt5.QtWinExtras import QtWin                                         #  !!!
        myappid = 'hptkop.kursova352.bilyi.denys'                          #  !!!
        QtWin.setCurrentProcessExplicitAppUserModelID(myappid)

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

        self.to_menu_button = QPushButton(self.centralwidget)
        self.to_menu_button.setObjectName(u"to_menu_button")
        self.to_menu_button.setGeometry(QRect(320, 390, 211, 51))

        font3 = QFont()
        font3.setPointSize(15)
        self.to_menu_button.setFont(font3)

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

        self.to_menu_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438 \u0434\u043e \u043c\u0435\u043d\u044e", None))

        self.label_4.setText("")
        self.label_5.setText("")

# Главное меню
class main_menu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon(u":/newPrefix/assets/start_menu_icon.png"))
        self.back_button.clicked.connect(self.to_start_func)
        self.exit_button.clicked.connect(exit_func)
        self.to_clients_button.clicked.connect(self.to_clients_func)
        self.to_workers_button.clicked.connect(self.to_workers_func)
        self.to_services_button.clicked.connect(self.to_services_func)
        self.to_materials_button.clicked.connect(self.to_materials_func)

    def to_materials_func(self):
        self.cams = materials()
        self.cams.show()
        self.close()

    def to_services_func(self):
        self.cams = services()
        self.cams.show()
        self.close()
    
    def to_workers_func(self):
        self.cams = workers()
        self.cams.show()
        self.close()

    def to_clients_func(self):
        self.cams = clients()
        self.cams.show()
        self.close()

    def to_start_func(self):
        self.cams = start()
        self.cams.show()
        self.close() 

    def setupUi(self, MainWindow):
        

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(356, 390)
        self.setWindowTitle('Головне меню')

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 20, 171, 41))

        font = QFont()
        font.setPointSize(19)
        self.label.setFont(font)

        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(0, 0, 41, 31))

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QSize(25, 25))
        self.back_button.setCheckable(False)
        self.back_button.setFlat(False)

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(320, 0, 41, 31))

        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit_button.setIcon(icon1)

        self.exit_button.setIconSize(QSize(25, 25))
        self.exit_button.setCheckable(False)
        self.exit_button.setFlat(False)

        self.to_clients_button = QPushButton(self.centralwidget)
        self.to_clients_button.setObjectName(u"to_clients_button")
        self.to_clients_button.setGeometry(QRect(110, 130, 121, 31))

        font1 = QFont()
        font1.setPointSize(14)
        self.to_clients_button.setFont(font1)

        self.to_offers_button = QPushButton(self.centralwidget)
        self.to_offers_button.setObjectName(u"to_offers_button")
        self.to_offers_button.setGeometry(QRect(110, 170, 121, 31))
        self.to_offers_button.setFont(font1)

        self.to_workers_button = QPushButton(self.centralwidget)
        self.to_workers_button.setObjectName(u"to_workers_button")
        self.to_workers_button.setGeometry(QRect(110, 210, 121, 31))
        self.to_workers_button.setFont(font1)

        self.to_materials_button = QPushButton(self.centralwidget)
        self.to_materials_button.setObjectName(u"to_materials_button")
        self.to_materials_button.setGeometry(QRect(110, 250, 121, 31))
        self.to_materials_button.setFont(font1)

        self.to_services_button = QPushButton(self.centralwidget)
        self.to_services_button.setObjectName(u"to_services_button")
        self.to_services_button.setGeometry(QRect(110, 290, 121, 31))
        self.to_services_button.setFont(font1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u043b\u043e\u0432\u043d\u0435 \u043c\u0435\u043d\u044e", None))
        self.back_button.setText("")
        self.exit_button.setText("")
        self.to_clients_button.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0456\u0454\u043d\u0442\u0438", None))
        self.to_offers_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0430\u0437\u0438", None))
        self.to_workers_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0438", None))
        self.to_materials_button.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0435\u0440\u0456\u0430\u043b\u0438", None))
        self.to_services_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0443\u0433\u0438", None))
    # retranslateUi

# Меню клиентов
class clients(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon(u":/newPrefix/assets/clients_icon.png"))

        self.back_button.clicked.connect(self.to_main_menu_func)
        self.exit_button.clicked.connect(exit_func)
        
        self.add_new_client_button.clicked.connect(self.to_add_client_func)
        self.view_clients_button.clicked.connect(self.to_clients_list_func)
    
    def to_clients_list_func(self):
        self.cams = clients_list()
        self.cams.show()
        self.close()

    def to_add_client_func(self):
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
        MainWindow.resize(333, 312)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.add_new_client_button = QPushButton(self.centralwidget)
        self.add_new_client_button.setObjectName(u"add_new_client_button")
        self.add_new_client_button.setGeometry(QRect(80, 80, 181, 31))

        font = QFont()
        font.setPointSize(11)

        self.add_new_client_button.setFont(font)

        self.view_clients_button = QPushButton(self.centralwidget)
        self.view_clients_button.setObjectName(u"view_clients_button")
        self.view_clients_button.setGeometry(QRect(80, 130, 181, 31))
        self.view_clients_button.setFont(font)

        self.clients_zvit_buttons = QPushButton(self.centralwidget)
        self.clients_zvit_buttons.setObjectName(u"clients_zvit_buttons")
        self.clients_zvit_buttons.setGeometry(QRect(80, 180, 181, 31))
        self.clients_zvit_buttons.setFont(font)

        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(0, 0, 41, 31))

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QSize(25, 25))
        self.back_button.setCheckable(False)
        self.back_button.setFlat(False)

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(290, 0, 41, 31))

        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit_button.setIcon(icon1)
        self.exit_button.setIconSize(QSize(25, 25))
        self.exit_button.setCheckable(False)
        self.exit_button.setFlat(False)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 10, 81, 31))

        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setWeight(50)

        self.label_2.setFont(font1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.add_new_client_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043d\u043e\u0432\u043e\u0433\u043e \u043a\u043b\u0456\u0454\u043d\u0442\u0430", None))
        self.view_clients_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0433\u043b\u044f\u0434 \u043a\u043b\u0456\u0454\u043d\u0442\u0456\u0432", None))
        self.clients_zvit_buttons.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0432\u0456\u0442\u043d\u0456\u0441\u0442\u044c \u043f\u043e \u043a\u043b\u0456\u0454\u0442\u0430\u043c", None))
        self.back_button.setText("")
        self.exit_button.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0456\u0454\u043d\u0442\u0438", None))
    # retranslateUi

# Добавить клиента
class add_client(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon(u":/newPrefix/assets/plus_icon.png"))
        self.back_button.clicked.connect(self.to_clients_func)
        self.exit_button.clicked.connect(exit_func)
        self.submit_button.clicked.connect(self.add_client_func)
        self.phone_field.setInputMask('999-999')

    def add_client_func(self):

        conn = sqlite3.connect("atelie.db") 
        name = self.name_field.text()
        phone = self.phone_field.text()

        if name == '' or phone == '' or phone == '-' or len(phone) < 7: 
            msg = QMessageBox()
            msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
            msg.setWindowTitle("Результат виконання")
            msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
            x = msg.exec_()
        else:

            try:
                with conn:
                    row = (name, phone)
                    # print('DATA =', row)      # for debugging

                    query = '''insert into Клієнти (ПІБ, Телефон)
                            values (?, ?);'''
                    conn.execute(query, row)

                    self.name_field.clear()
                    self.phone_field.clear()

                    msg = QMessageBox()
                    msg.setWindowIcon(QIcon(u":/newPrefix/assets/success_icon.png"))
                    msg.setWindowTitle("Результат виконання")
                    msg.setText("Операція виконана успішно!")
                    x = msg.exec_() 

            except sqlite3.Error as e:
                # print(e)              for debugging
                # print(e.args)

                self.name_field.clear()
                self.phone_field.clear()

                msg = QMessageBox()
                msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
                msg.setWindowTitle("Результат виконання")
                msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
                x = msg.exec_() 

            conn.commit()
            conn.close()
        
    def to_clients_func(self):
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

        self.name_field = QLineEdit(self.centralwidget)
        self.name_field.setObjectName(u"name_field")
        self.name_field.setGeometry(QRect(190, 130, 261, 41))

        font = QFont()
        font.setPointSize(12)
        self.name_field.setFont(font)

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

        self.phone_field = QLineEdit(self.centralwidget)
        self.phone_field.setObjectName(u"phone_field")
        self.phone_field.setGeometry(QRect(190, 190, 261, 31))
        self.phone_field.setFont(font)

        self.submit_button = QPushButton(self.centralwidget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(350, 250, 101, 31))
        self.submit_button.setFont(font1)

        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(0, 0, 41, 31))
        
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 0, 201, 41))
        font3 = QFont()
        font3.setPointSize(16)
        self.label_3.setFont(font3)

        font2 = QFont()
        font2.setPointSize(2)

        self.back_button.setFont(font2)

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QSize(25, 25))

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(530, 0, 41, 31))
        self.exit_button.setFont(font2)

        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit_button.setIcon(icon1)
        self.exit_button.setIconSize(QSize(25, 25))

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
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438", None))
        self.back_button.setText("")
        self.exit_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043a\u043b\u0456\u0454\u043d\u0442\u0430", None))
    # retranslateUi

# Редактировать клиента
class edit_client(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(u":/newPrefix/assets/plus_icon.png"))

        self.submit_button.clicked.connect(self.edit_func)
        self.cancel_button.clicked.connect(self.cancel_func)
        self.code = None

    def set_code(self, code):
        self.code = code

    def cancel_func(self):
        self.close()

    def edit_func(self):
        name = self.name_field.text()
        phone = self.phone_field.text()
        code = self.code
        print('DATA = ',name,phone,code)
        
        if name == '' or phone == '-' or len(phone) < 7:
            msg = QMessageBox()
            msg.setWindowTitle("Результат виконання")
            msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
            msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
            x = msg.exec_() 
        else:
            try:
                conn = sqlite3.connect("atelie.db") 
                with conn:

                    query = '''UPDATE Клієнти SET ПІБ = ?, Телефон = ? WHERE Код_клієнта = ?;'''
                    conn.execute(query, (name,phone,code) )

                    msg = QMessageBox()
                    msg.setWindowTitle("Результат виконання")
                    msg.setWindowIcon(QIcon(u":/newPrefix/assets/success_icon.png"))
                    msg.setText("Операція виконана успішно!")
                    x = msg.exec_() 
                    # self.tableWidget.removeRow(current_row)

            except sqlite3.Error as e:
                # print(e)              #for debugging
                # print(e.args)

                msg = QMessageBox()
                msg.setWindowTitle("Результат виконання")
                msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
                msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
                x = msg.exec_() 
                
            conn.commit()
            conn.close()
            self.close()

        
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(567, 348)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 10, 221, 31))

        font = QFont()
        font.setPointSize(17)
    
        self.label.setFont(font)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 101, 61))

        font1 = QFont()
        font1.setPointSize(13)

        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 140, 101, 61))
        self.label_3.setFont(font1)

        self.name_field = QLineEdit(self.centralwidget)
        self.name_field.setObjectName(u"name_field")
        self.name_field.setGeometry(QRect(140, 90, 341, 31))

        font2 = QFont()
        font2.setPointSize(11)

        self.name_field.setFont(font2)

        self.phone_field = QLineEdit(self.centralwidget)
        self.phone_field.setObjectName(u"phone_field")
        self.phone_field.setGeometry(QRect(140, 150, 341, 31))
        self.phone_field.setFont(font2)

        self.submit_button = QPushButton(self.centralwidget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(180, 260, 131, 31))
        self.submit_button.setFont(font1)

        self.cancel_button = QPushButton(self.centralwidget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(330, 260, 131, 31))
        self.cancel_button.setFont(font1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u043d\u043e\u0432\u0456 \u0434\u0430\u043d\u0456", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0406\u0411 \u043a\u043b\u0456\u0454\u043d\u0442\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.phone_field.setInputMask(QCoreApplication.translate("MainWindow", u"999-999", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0456\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0438", None))
        self.cancel_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0438\u0442\u0438", None))
    # retranslateUi
# Просмотр клиентов
class clients_list(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

        self.setWindowIcon(QIcon(u":/newPrefix/assets/list_icon.png"))

        self.back_button.clicked.connect(self.to_clients_func)
        self.exit_button.clicked.connect(exit_func)
        self.down_button.clicked.connect(self.next_item_func)
        self.up_button.clicked.connect(self.previous_item_func)
        self.find_button.clicked.connect(self.search_func)
        self.update_button.clicked.connect(self.load_data_func)
        self.delete_button.clicked.connect(self.delete_func)
        self.tableWidget.clicked.connect(self.currention_func)
        self.edit_button.clicked.connect(self.edit_func)

    def edit_func(self):

        code = self.tableWidget.item(self.tableWidget.currentRow(),self.tableWidget.currentColumn()).text()
        self.cams = edit_client()
        self.cams.set_code(code=code)
        self.cams.show()
        
    def currention_func(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow())

    def next_item_func(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow()+1)
        
    def previous_item_func(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow()-1)

    def delete_func(self):
        # current_row = self.tableWidget.currentRow()
        code = self.tableWidget.item(self.tableWidget.currentRow(),self.tableWidget.currentColumn()).text()
        conn = sqlite3.connect("atelie.db") 

        try:
            with conn:
                
                # print('DATA =', code)      # for debugging

                query = '''DELETE FROM Клієнти WHERE Код_клієнта=?;'''
                conn.execute(query, (code,) )

                msg = QMessageBox()
                msg.setWindowTitle("Результат виконання")
                msg.setWindowIcon(QIcon(u":/newPrefix/assets/success_icon.png"))
                msg.setText("Операція виконана успішно!")
                x = msg.exec_() 
                # self.tableWidget.removeRow(current_row)

        except sqlite3.Error as e:
            # print(e)              #for debugging
            # print(e.args)

            msg = QMessageBox()
            msg.setWindowTitle("Результат виконання")
            msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
            msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
            x = msg.exec_() 
            
        conn.commit()
        conn.close()
        self.load_data_func()

    def to_clients_func(self):
        self.cams = clients()
        self.cams.show()
        self.close()  
        
    def load_data_func(self):
        self.tableWidget.setRowCount(0)
        # print('Rows set to 0')   for debugging
        connection = sqlite3.connect("atelie.db")
        cur = connection.cursor()
        sqlquery = "SELECT * FROM Клієнти"
        tablerow = 0
        total_rows_count = 0

        for row in cur.execute(sqlquery):
            total_rows_count += 1

        self.tableWidget.setRowCount(total_rows_count)
        # print(f'rows set to {total_rows_count}')      for debugging

        for row in cur.execute(sqlquery):

                    # print(row)        for debugging
            self.tableWidget.setItem(tablerow,0,QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow,1,QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow,2,QTableWidgetItem(row[2]))
            tablerow += 1
        QTimer.singleShot(10000, self.load_data_func)
        # print('data loaded ')     for debugging

    def search_func(self):

        items = self.tableWidget.findItems(self.find_field.text(), Qt.MatchExactly)
        if items:
            self.tableWidget.selectRow(items[0].row())
        else:
            QMessageBox.information(self, 'Search Results', 'Нічого не знайдено. Спробуйте ще раз')
            
            
                    # print('err')        for debugging
        


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

        self.load_data_func()

        self.delete_button = QPushButton(self.centralwidget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(450, 350, 141, 31))

        font4 = QFont()
        font4.setPointSize(12)

        self.delete_button.setFont(font4)

        self.update_button = QPushButton(self.centralwidget)
        self.update_button.setObjectName(u"update_button")
        self.update_button.setGeometry(QRect(610, 350, 141, 31))
        self.update_button.setFont(font4)

        self.edit_button = QPushButton(self.centralwidget)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setGeometry(QRect(300, 350, 141, 31))
        self.edit_button.setFont(font4)

        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(0, 0, 41, 31))

        font = QFont()
        font.setPointSize(2)

        self.back_button.setFont(font)

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QSize(25, 25))

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(760, 0, 41, 31))
        self.exit_button.setFont(font)

        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit_button.setIcon(icon1)
        self.exit_button.setIconSize(QSize(25, 25))

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 10, 101, 31))
        
        font1 = QFont()
        font1.setPointSize(17)

        self.label.setFont(font1)

        self.up_button = QPushButton(self.centralwidget)
        self.up_button.setObjectName(u"up_button")
        self.up_button.setGeometry(QRect(10, 150, 41, 41))

        font2 = QFont()
        font2.setPointSize(13)

        self.up_button.setFont(font2)

        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/assets/up_arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.up_button.setIcon(icon2)
        self.up_button.setIconSize(QSize(30, 30))

        self.down_button = QPushButton(self.centralwidget)
        self.down_button.setObjectName(u"down_button")
        self.down_button.setGeometry(QRect(10, 190, 41, 41))

        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/assets/down_arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.down_button.setIcon(icon3)
        self.down_button.setIconSize(QSize(30, 30))

        self.find_field = QLineEdit(self.centralwidget)
        self.find_field.setObjectName(u"find_edit")
        self.find_field.setGeometry(QRect(160, 350, 71, 21))

        font3 = QFont()
        font3.setPointSize(10)

        self.find_field.setFont(font3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 350, 111, 21))
        self.label_2.setFont(font2)

        self.find_button = QPushButton(self.centralwidget)
        self.find_button.setObjectName(u"find_button")
        self.find_button.setGeometry(QRect(160, 380, 71, 31))
        self.find_button.setFont(font2)

        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        self.back_button.setText("")
        self.exit_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0456\u0454\u043d\u0442\u0438", None))
        self.up_button.setText("")
        self.down_button.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u043a\u043b\u0456\u0454\u043d\u0442\u0430", None))
        self.find_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0448\u0443\u043a", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0437\u0430\u043f\u0438\u0441", None))
        self.update_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043d\u043e\u0432\u0438\u0442\u0438 \u0442\u0430\u0431\u043b\u0438\u0446\u044e", None))
        self.edit_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043c\u0456\u043d\u0438\u0442\u0438", None))
    # retranslateUi

# Меню работников
class workers(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back_button.clicked.connect(self.to_main_menu_func)
        self.exit_button.clicked.connect(exit_func)
        self.view_workers_button.clicked.connect(self.to_workers_list_func)
        self.add_new_worker_button.clicked.connect(self.to_add_worker_func)

    def to_add_worker_func(self):
        self.cams = add_workers()
        self.cams.show()
        self.close()

    def to_workers_list_func(self):
        self.cams = workers_list()
        self.cams.show()
        self.close()

    def to_main_menu_func(self):
        self.cams = main_menu()
        self.cams.show()
        self.close()

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(331, 296)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.add_new_worker_button = QPushButton(self.centralwidget)
        self.add_new_worker_button.setObjectName(u"add_new_worker_button")
        self.add_new_worker_button.setGeometry(QRect(70, 150, 181, 31))

        font = QFont()
        font.setPointSize(10)

        self.add_new_worker_button.setFont(font)

        self.workers_analisys_button = QPushButton(self.centralwidget)
        self.workers_analisys_button.setObjectName(u"workers_analisys_button")
        self.workers_analisys_button.setGeometry(QRect(70, 200, 181, 31))
        self.workers_analisys_button.setFont(font)

        self.view_workers_button = QPushButton(self.centralwidget)
        self.view_workers_button.setObjectName(u"view_workers_button")
        self.view_workers_button.setGeometry(QRect(70, 100, 181, 31))
        self.view_workers_button.setFont(font)

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(290, 0, 41, 31))

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit_button.setIcon(icon)
        self.exit_button.setIconSize(QSize(25, 25))
        self.exit_button.setCheckable(False)
        self.exit_button.setFlat(False)

        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(0, 0, 41, 31))

        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back_button.setIcon(icon1)
        self.back_button.setIconSize(QSize(25, 25))
        self.back_button.setCheckable(False)
        self.back_button.setFlat(False)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 10, 141, 31))

        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setWeight(50)

        self.label.setFont(font1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Працівники", u"Працівники", None))
        self.add_new_worker_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043d\u043e\u0432\u043e\u0433\u043e \u043f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0430", None))
        self.workers_analisys_button.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0456\u0437 \u043f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0456\u0432", None))
        self.view_workers_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0433\u043b\u044f\u0434 \u043f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0456\u0432", None))
        self.exit_button.setText("")
        self.back_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0438", None))
    # retranslateUi

# Просмотр работников
class workers_list(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(u":/newPrefix/assets/list_icon.png"))

        self.back_button.clicked.connect(self.to_workers_func)
        self.exit_button.clicked.connect(exit_func)
        self.up_button.clicked.connect(self.previous_item_func)
        self.down_button.clicked.connect(self.next_item_func)
        self.find_button.clicked.connect(self.search_func)
        self.delete_button.clicked.connect(self.delete_func)
        self.update_button.clicked.connect(self.load_data_func)
        self.tableWidget.clicked.connect(self.currention_func)
        self.edit_button.clicked.connect(self.edit_func)
    
    def edit_func(self):
        code = self.tableWidget.item(self.tableWidget.currentRow(),self.tableWidget.currentColumn()).text()
        self.cams = edit_worker()
        self.cams.set_code(code)
        self.cams.show()

    def currention_func(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow())

    def next_item_func(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow()+1)
        
    def previous_item_func(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow()-1)

    def search_func(self):
        items = self.tableWidget.findItems(self.find_field.text(), Qt.MatchExactly)
        if items:
            self.tableWidget.selectRow(items[0].row())
        else:
            QMessageBox.information(self, 'Search Results', 'Нічого не знайдено. Спробуйте ще раз')
            # print('err')        for debugging
                    

    def delete_func(self):
        current_row = self.tableWidget.currentRow()
        code = self.tableWidget.item(self.tableWidget.currentRow(),self.tableWidget.currentColumn()).text()
        conn = sqlite3.connect("atelie.db") 

        try:
            with conn:
                
                # print('DATA =', code)      # for debugging

                query = '''DELETE FROM Працівники WHERE Код_працівника=?;'''
                conn.execute(query, (code,) )

                msg = QMessageBox()
                msg.setWindowTitle("Результат виконання")
                msg.setWindowIcon(QIcon(u":/newPrefix/assets/success_icon.png"))
                msg.setText("Операція виконана успішно!")
                x = msg.exec_() 
                self.tableWidget.removeRow(current_row)

        except sqlite3.Error as e:
            # print(e)              #for debugging
            # print(e.args)

            msg = QMessageBox()
            msg.setWindowTitle("Результат виконання")
            msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
            msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
            x = msg.exec_() 
            
        conn.commit()
        conn.close()

    def load_data_func(self):
        self.tableWidget.setRowCount(0)
        # print('Rows set to 0')   for debugging
        connection = sqlite3.connect("atelie.db")
        cur = connection.cursor()
        sqlquery = "SELECT * FROM Працівники"
        tablerow = 0
        total_rows_count = 0

        for row in cur.execute(sqlquery):
            total_rows_count += 1

        self.tableWidget.setRowCount(total_rows_count)
        # print(f'rows set to {total_rows_count}')      for debugging

        for row in cur.execute(sqlquery):

                    # print(row)        for debugging
            self.tableWidget.setItem(tablerow,0,QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow,1,QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tablerow,2,QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(tablerow,3,QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow,4,QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tablerow,5,QTableWidgetItem(str(row[5])+' ₴'))

            tablerow += 1
        QTimer.singleShot(10000, self.load_data_func)
        # print('data loaded ')     for debugging


    def to_workers_func(self):
        self.cams = workers()
        self.cams.show()
        self.close()

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(798, 445)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 10, 161, 31))

        font = QFont()
        font.setPointSize(17)

        self.label.setFont(font)

        self.down_button = QPushButton(self.centralwidget)
        self.down_button.setObjectName(u"down_button")
        self.down_button.setGeometry(QRect(10, 190, 41, 41))

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/down_arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.down_button.setIcon(icon)
        self.down_button.setIconSize(QSize(30, 30))

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 350, 131, 21))

        font1 = QFont()
        font1.setPointSize(13)

        self.label_2.setFont(font1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(80, 50, 671, 291))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setColumnWidth(1,250)
        self.tableWidget.setColumnWidth(2,50)
        self.tableWidget.setColumnWidth(4,80)
        self.tableWidget.setColumnWidth(5,80)
        self.tableWidget.setColumnWidth(6,80)
        self.tableWidget.setHorizontalHeaderLabels(["Код працівника","ПІБ","Стаж","Телефон","Стать","Зарплата"])
        self.tableWidget.verticalHeader().setVisible(False)

        self.load_data_func()

        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(0, 0, 41, 31))

        font2 = QFont()
        font2.setPointSize(2)
    
        self.back_button.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back_button.setIcon(icon1)
        self.back_button.setIconSize(QSize(25, 25))

        self.up_button = QPushButton(self.centralwidget)
        self.up_button.setObjectName(u"up_button")
        self.up_button.setGeometry(QRect(10, 150, 41, 41))
        self.up_button.setFont(font1)

        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/assets/up_arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.up_button.setIcon(icon2)
        self.up_button.setIconSize(QSize(30, 30))

        self.find_button = QPushButton(self.centralwidget)
        self.find_button.setObjectName(u"find_button")
        self.find_button.setGeometry(QRect(210, 380, 71, 31))
        self.find_button.setFont(font1)

        self.delete_button = QPushButton(self.centralwidget)
        self.delete_button.setObjectName(u"delete_2")
        self.delete_button.setGeometry(QRect(450, 350, 141, 31))
        font3 = QFont()
        font3.setPointSize(12)
        self.delete_button.setFont(font3)

        self.update_button = QPushButton(self.centralwidget)
        self.update_button.setObjectName(u"update_button")
        self.update_button.setGeometry(QRect(610, 350, 141, 31))
        self.update_button.setFont(font3)

        self.find_field = QLineEdit(self.centralwidget)
        self.find_field.setObjectName(u"find_field")
        self.find_field.setGeometry(QRect(210, 350, 71, 21))
        
        font4 = QFont()
        font4.setPointSize(10)
        self.find_field.setFont(font4)

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(760, 0, 41, 31))
        self.exit_button.setFont(font2)

        self.edit_button = QPushButton(self.centralwidget)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setGeometry(QRect(320, 350, 121, 31))
        self.edit_button.setFont(font3)
    
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIconSize(QSize(25, 25))
        self.exit_button.setIcon(icon3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):

        MainWindow.setWindowTitle(QCoreApplication.translate("Список працівників", u"Список працівників", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0438", None))
        self.down_button.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u043f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0430", None))
        self.back_button.setText("")
        self.up_button.setText("")
        self.find_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0448\u0443\u043a", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0437\u0430\u043f\u0438\u0441", None))
        self.update_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043d\u043e\u0432\u0438\u0442\u0438 \u0442\u0430\u0431\u043b\u0438\u0446\u044e", None))
        self.exit_button.setText("")
        self.edit_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043c\u0456\u043d\u0438\u0442\u0438", None))
    # retranslateUi

# Добавить работника
class add_workers(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(u":/newPrefix/assets/plus_icon.png"))

        self.back_button.clicked.connect(self.to_workers_func)
        self.exit_button.clicked.connect(exit_func)
        self.submit_button.clicked.connect(self.add_worker_func)
        self.phone_field.setInputMask('999-999')
        self.phone_field.setMaxLength(7)

    def to_workers_func(self):
        self.cams = workers()
        self.cams.show()
        self.close()

    def add_worker_func(self):
        
        conn = sqlite3.connect("atelie.db") 
        name = self.name_field.text()
        stazh = self.stazh_field.text()
        sex = self.sex_field.text()
        salary = self.salary_field.text()
        phone = self.phone_field.text()

        try:
            with conn:
                row = (name, stazh, phone, sex, salary)
                print('DATA =', row)      # for debugging

                query = '''insert into Працівники (ПІБ_працівника, Стаж, Телефон, Стать, Зарплата)
                            values (?, ?, ?, ?, ?);'''
                conn.execute(query, row)

                self.name_field.clear()
                self.phone_field.clear()
                self.stazh_field.clear()
                self.sex_field.clear()
                self.salary_field.clear()

                msg = QMessageBox()
                msg.setWindowIcon(QIcon(u":/newPrefix/assets/success_icon.png"))
                msg.setWindowTitle("Результат виконання")
                msg.setText("Операція виконана успішно!")
                x = msg.exec_() 

        except sqlite3.Error as e:
            # print(e)              for debugging
            # print(e.args)

            self.name_field.clear()
            self.phone_field.clear()

            msg = QMessageBox()
            msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
            msg.setWindowTitle("Результат виконання")
            msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
            x = msg.exec_() 

        conn.commit()
        conn.close()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(572, 456)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.stazh_field = QLineEdit(self.centralwidget)
        self.stazh_field.setObjectName(u"stazh_field")
        self.stazh_field.setGeometry(QRect(230, 160, 261, 31))

        font = QFont()
        font.setPointSize(12)

        self.stazh_field.setFont(font)

        self.name_field = QLineEdit(self.centralwidget)
        self.name_field.setObjectName(u"name_field")
        self.name_field.setGeometry(QRect(230, 100, 261, 41))
        self.name_field.setFont(font)

        self.submit_button = QPushButton(self.centralwidget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(390, 380, 101, 31))

        font1 = QFont()
        font1.setPointSize(11)

        self.submit_button.setFont(font1)

        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back")
        self.back_button.setGeometry(QRect(0, 0, 41, 31))

        font2 = QFont()
        font2.setPointSize(2)

        self.back_button.setFont(font2)

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QSize(25, 25))

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 110, 191, 31))
        self.label.setFont(font1)

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit")
        self.exit_button.setGeometry(QRect(530, 0, 41, 31))
        self.exit_button.setFont(font2)

        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit_button.setIcon(icon1)
        self.exit_button.setIconSize(QSize(25, 25))

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 160, 191, 31))
        self.label_2.setFont(font1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(210, 10, 201, 41))

        font3 = QFont()
        font3.setPointSize(16)

        self.label_4.setFont(font3)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 210, 201, 31))
        self.label_3.setFont(font1)

        self.phone_field = QLineEdit(self.centralwidget)
        self.phone_field.setObjectName(u"phone_field")
        self.phone_field.setGeometry(QRect(230, 210, 261, 31))
        self.phone_field.setFont(font)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 260, 201, 31))
        self.label_5.setFont(font1)

        self.sex_field = QLineEdit(self.centralwidget)
        self.sex_field.setObjectName(u"sex_field")
        self.sex_field.setGeometry(QRect(230, 260, 261, 31))
        self.sex_field.setFont(font)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 320, 201, 31))
        self.label_6.setFont(font1)

        self.salary_field = QLineEdit(self.centralwidget)
        self.salary_field.setObjectName(u"salary_field")
        self.salary_field.setGeometry(QRect(230, 320, 261, 31))
        self.salary_field.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Додати працівника", u"Додати працівника", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438", None))
        self.back_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u041f\u0406\u0411 \u043f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0430", None))
        self.exit_button.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0441\u0442\u0430\u0436 \u043f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0442\u0435\u043b\u0435\u0444\u043e\u043d \u043f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0430", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0441\u0442\u0430\u0442\u044c \u043f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0430", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0437\u0430\u0440\u043f\u043b\u0430\u0442\u0443 \u043f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0430", None))
    # retranslateUi

# Редактировать работника
class edit_worker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(u":/newPrefix/assets/plus_icon.png"))

        self.cancel_button.clicked.connect(self.cancel_func)
        self.submit_button.clicked.connect(self.edit_worker_func)
        self.code = None

    def set_code(self, code):
        self.code = code

    def cancel_func(self):
        self.close()
    
    def edit_worker_func(self):
        name = self.name_field.text()
        phone = self.phone_field.text()
        stazh = self.stazh_field.text()
        salary = self.salary_field.text()
        code = self.code
        if self.sex_male_rb.isChecked():
            sex = 'м'
        elif self.sex_female_rb.isChecked():
            sex = 'ж'
        else:
            sex = ''

        #print('DATA = ',name,stazh,phone,sex,salary,code)   # for debugging
        
        if name == '' or phone == '-' or len(phone) < 7 or stazh == '' or salary == '' or sex == '':
            msg = QMessageBox()
            msg.setWindowTitle("Результат виконання")
            msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
            msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
            x = msg.exec_() 
        else:
            try:
                conn = sqlite3.connect("atelie.db") 
                with conn:

                    query = '''UPDATE Працівники SET ПІБ_працівника = ?, Стаж = ?, Телефон = ?, Стать = ?, Зарплата = ? WHERE Код_працівника = ?;'''
                    conn.execute(query, (name,stazh,phone,sex,salary,code) )

                    msg = QMessageBox()
                    msg.setWindowTitle("Результат виконання")
                    msg.setWindowIcon(QIcon(u":/newPrefix/assets/success_icon.png"))
                    msg.setText("Операція виконана успішно!")
                    x = msg.exec_() 
                    # self.tableWidget.removeRow(current_row)

            except sqlite3.Error as e:
                # print(e)              #for debugging
                # print(e.args)

                msg = QMessageBox()
                msg.setWindowTitle("Результат виконання")
                msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
                msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
                x = msg.exec_() 
                
            conn.commit()
            conn.close()
            self.close()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(958, 346)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 70, 131, 61))

        font = QFont()
        font.setPointSize(13)

        self.label_5.setFont(font)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 120, 101, 61))
        self.label_4.setFont(font)

        self.name_field = QLineEdit(self.centralwidget)
        self.name_field.setObjectName(u"name_field")
        self.name_field.setGeometry(QRect(150, 90, 251, 31))

        font1 = QFont()
        font1.setPointSize(11)

        self.name_field.setFont(font1)

        self.phone_field = QLineEdit(self.centralwidget)
        self.phone_field.setObjectName(u"phone_field")
        self.phone_field.setGeometry(QRect(150, 140, 251, 31))
        self.phone_field.setFont(font1)

        self.cancel_button = QPushButton(self.centralwidget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(480, 250, 131, 31))
        self.cancel_button.setFont(font)

        self.submit_button = QPushButton(self.centralwidget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(330, 250, 131, 31))
        self.submit_button.setFont(font)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(350, 20, 221, 31))

        font2 = QFont()
        font2.setPointSize(17)

        self.label_6.setFont(font2)

        self.stazh_field = QLineEdit(self.centralwidget)
        self.stazh_field.setObjectName(u"stazh_field")
        self.stazh_field.setGeometry(QRect(490, 90, 121, 31))
        self.stazh_field.setFont(font1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(430, 70, 101, 61))
        self.label_7.setFont(font)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(430, 130, 61, 61))
        self.label_8.setFont(font)

        self.salary_field = QLineEdit(self.centralwidget)
        self.salary_field.setObjectName(u"salary_field")
        self.salary_field.setGeometry(QRect(730, 90, 121, 31))
        self.salary_field.setFont(font1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(640, 70, 101, 61))
        self.label_9.setFont(font)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(490, 140, 120, 31))
        self.groupBox.setFlat(False)

        self.sex_female_rb = QRadioButton(self.groupBox)
        self.sex_female_rb.setObjectName(u"sex_female_rb")
        self.sex_female_rb.setGeometry(QRect(60, 10, 31, 17))

        self.sex_male_rb = QRadioButton(self.groupBox)
        self.sex_male_rb.setObjectName(u"sex_male_rb")
        self.sex_male_rb.setGeometry(QRect(10, 10, 31, 17))

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0406\u0411 \u043f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.phone_field.setInputMask(QCoreApplication.translate("MainWindow", u"999-999", None))
        self.cancel_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0438\u0442\u0438", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0456\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0438", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u043d\u043e\u0432\u0456 \u0434\u0430\u043d\u0456", None))
        self.stazh_field.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0436", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u044c", None))
        self.salary_field.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u043f\u043b\u0430\u0442\u0430", None))
        self.groupBox.setTitle("")
        self.sex_female_rb.setText(QCoreApplication.translate("MainWindow", u"\u0416", None))
        self.sex_male_rb.setText(QCoreApplication.translate("MainWindow", u"\u041c", None))
    # retranslateUi

# Меню услуг
class services(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back_button.clicked.connect(self.to_main_menu_func)
        self.exit_button.clicked.connect(exit_func)
        self.to_view_products_button.clicked.connect(self.to_products_func)
        self.to_view_repair_services_button.clicked.connect(self.to_repairs_func)
        self.add_product_button.clicked.connect(self.to_add_products_func)

    
    def to_repairs_func(self):
        pass
    
    def to_products_func(self):
        self.cams = products_list()
        self.cams.show()
        self.close()

    def to_add_products_func(self):
        self.cams = add_product()
        self.cams.show()
        self.close()
    
    def to_main_menu_func(self):
        self.cams = main_menu()
        self.cams.show()
        self.close()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(337, 298)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(300, 0, 41, 31))

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit_button.setIcon(icon)
        self.exit_button.setIconSize(QSize(25, 25))
        self.exit_button.setCheckable(False)
        self.exit_button.setFlat(False)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 10, 101, 31))

        font = QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.label_2.setFont(font)

        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(0, 0, 41, 31))

        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back_button.setIcon(icon1)
        self.back_button.setIconSize(QSize(25, 25))
        self.back_button.setCheckable(False)
        self.back_button.setFlat(False)

        self.to_view_repair_services_button = QPushButton(self.centralwidget)
        self.to_view_repair_services_button.setObjectName(u"to_view_repair_services_button")
        self.to_view_repair_services_button.setGeometry(QRect(80, 70, 181, 31))

        font1 = QFont()
        font1.setPointSize(10)

        self.to_view_repair_services_button.setFont(font1)

        self.to_view_products_button = QPushButton(self.centralwidget)
        self.to_view_products_button.setObjectName(u"to_view_products_button")
        self.to_view_products_button.setGeometry(QRect(80, 110, 181, 31))
        self.to_view_products_button.setFont(font1)

        self.add_repair_service_button = QPushButton(self.centralwidget)
        self.add_repair_service_button.setObjectName(u"add_repair_service_button")
        self.add_repair_service_button.setGeometry(QRect(80, 150, 181, 31))
        self.add_repair_service_button.setFont(font1)

        self.add_product_button = QPushButton(self.centralwidget)
        self.add_product_button.setObjectName(u"add_product_button")
        self.add_product_button.setGeometry(QRect(80, 190, 181, 31))
        self.add_product_button.setFont(font1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Послуги", u"Послуги", None))
        self.exit_button.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0443\u0433\u0438", None))
        self.back_button.setText("")
        self.to_view_repair_services_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0433\u043b\u044f\u0434 \u043f\u043e\u0441\u043b\u0443\u0433 \u0440\u0435\u043c\u043e\u043d\u0442\u0443", None))
        self.to_view_products_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0433\u043b\u044f\u0434 \u0432\u0438\u0440\u043e\u0431\u0456\u0432", None))
        self.add_repair_service_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043f\u043e\u0441\u043b\u0443\u0433\u0443 \u0440\u0435\u043c\u043e\u043d\u0442\u0443", None))
        self.add_product_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u0432\u0438\u0440\u0456\u0431", None))
    # retranslateUi

class materials(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back_button.clicked.connect(self.to_main_menu_func)
        self.exit_button.clicked.connect(exit_func)
        self.view_materials_button.clicked.connect(self.to_view_materials_func)
        self.add_new_material_button.clicked.connect(self.to_add_material_func)


    def to_main_menu_func(self):
        self.cams = main_menu()
        self.cams.show()
        self.close()

    def to_view_materials_func(self):
        self.cams = materials_list()
        self.cams.show()
        self.close()
    
    def to_add_material_func(self):
        self.cams = add_material()
        self.cams.show()
        self.close()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(332, 255)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 10, 121, 31))

        font = QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)

        self.label_3.setFont(font)

        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(0, 0, 41, 31))

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QSize(25, 25))
        self.back_button.setCheckable(False)
        self.back_button.setFlat(False)

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(290, 0, 41, 31))

        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit_button.setIcon(icon1)
        self.exit_button.setIconSize(QSize(25, 25))
        self.exit_button.setCheckable(False)
        self.exit_button.setFlat(False)

        self.add_new_material_button = QPushButton(self.centralwidget)
        self.add_new_material_button.setObjectName(u"add_new_material_button")
        self.add_new_material_button.setGeometry(QRect(80, 100, 181, 31))

        font1 = QFont()
        font1.setPointSize(11)

        self.add_new_material_button.setFont(font1)

        self.view_materials_button = QPushButton(self.centralwidget)
        self.view_materials_button.setObjectName(u"view_materials_button")
        self.view_materials_button.setGeometry(QRect(80, 150, 181, 31))
        self.view_materials_button.setFont(font1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Матеріали", u"Матеріали", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0435\u0440\u0456\u0430\u043b\u0438", None))
        self.back_button.setText("")
        self.exit_button.setText("")
        self.add_new_material_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043c\u0430\u0442\u0435\u0440\u0456\u0430\u043b", None))
        self.view_materials_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0433\u043b\u044f\u0434 \u043c\u0430\u0442\u0435\u0440\u0456\u0430\u043b\u0456\u0432", None))
    # retranslateUi

class add_material(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back_button.clicked.connect(self.to_materials_func)
        self.exit_button.clicked.connect(exit_func)
        self.submit_button.clicked.connect(self.add_material_func)
    
    def to_materials_func(self):
        self.cams = materials()
        self.cams.show()
        self.close()

    def add_material_func(self):
        conn = sqlite3.connect("atelie.db") 
        name = self.name_field.text()
        producer = self.producer_field.text()
        

        try:
            with conn:
                row = (name, producer)
                print('DATA =', row)      # for debugging

                query = '''insert into Матеріали (Назва, Виробник)
                            values (?, ?);'''
                conn.execute(query, row)

                self.name_field.clear()
                self.producer_field.clear()
                

                msg = QMessageBox()
                msg.setWindowIcon(QIcon(u":/newPrefix/assets/success_icon.png"))
                msg.setWindowTitle("Результат виконання")
                msg.setText("Операція виконана успішно!")
                x = msg.exec_() 

        except sqlite3.Error as e:
            # print(e)              for debugging
            # print(e.args)

            self.name_field.clear()
            self.producer_field.clear()

            msg = QMessageBox()
            msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
            msg.setWindowTitle("Результат виконання")
            msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
            x = msg.exec_() 

        conn.commit()
        conn.close()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(572, 264)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(530, 0, 41, 31))

        font = QFont()
        font.setPointSize(2)

        self.exit_button.setFont(font)

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit_button.setIcon(icon)
        self.exit_button.setIconSize(QSize(25, 25))

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(190, 10, 171, 41))

        font1 = QFont()
        font1.setPointSize(16)

        self.label_7.setFont(font1)

        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(0, 0, 41, 31))
        self.back_button.setFont(font)

        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back_button.setIcon(icon1)
        self.back_button.setIconSize(QSize(25, 25))

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 90, 191, 31))

        font2 = QFont()
        font2.setPointSize(11)

        self.label_8.setFont(font2)

        self.name_field = QLineEdit(self.centralwidget)
        self.name_field.setObjectName(u"name_field")
        self.name_field.setGeometry(QRect(250, 90, 261, 31))

        font3 = QFont()
        font3.setPointSize(12)

        self.name_field.setFont(font3)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 130, 191, 31))
        self.label_9.setFont(font2)

        self.producer_field = QLineEdit(self.centralwidget)
        self.producer_field.setObjectName(u"producer_field")
        self.producer_field.setGeometry(QRect(250, 130, 261, 31))
        self.producer_field.setFont(font3)

        self.submit_button = QPushButton(self.centralwidget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(410, 190, 101, 31))
        self.submit_button.setFont(font2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.exit_button.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043c\u0430\u0442\u0435\u0440\u0456\u0430\u043b", None))
        self.back_button.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u043d\u0430\u0437\u0432\u0443 \u043c\u0430\u0442\u0435\u0440\u0456\u0430\u043b\u0443", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0432\u0438\u0440\u043e\u0431\u043d\u0438\u043a\u0430 \u043c\u0430\u0442\u0435\u0440\u0456\u0430\u043b\u0443", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438", None))
    # retranslateUi

class materials_list(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back_button.clicked.connect(self.to_materials_func)
        self.exit_button.clicked.connect(exit_func)
        self.up_button.clicked.connect(self.previous_item_func)
        self.down_button.clicked.connect(self.next_item_func)
        self.find_button.clicked.connect(self.search_func)
        self.edit_button.clicked.connect(self.edit_func)
        self.delete_button.clicked.connect(self.delete_func)
        self.update_button.clicked.connect(self.update_func)
        self.tableWidget.clicked.connect(self.currention_func)
    
    def edit_func(self):
        code = self.tableWidget.item(self.tableWidget.currentRow(),self.tableWidget.currentColumn()).text()
        self.cams = edit_material()
        self.cams.set_code(code)
        self.cams.show()

    def update_func(self):
        self.load_data_func()

    def to_materials_func(self):
        self.cams = materials()
        self.cams.show()
        self.close()
    
    def previous_item_func(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow()-1)
    
    def next_item_func(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow()+1)

    def currention_func(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow())

    def delete_func(self):
        # current_row = self.tableWidget.currentRow()
        code = self.tableWidget.item(self.tableWidget.currentRow(),self.tableWidget.currentColumn()).text()
        conn = sqlite3.connect("atelie.db") 

        try:
            with conn:
                
                # print('DATA =', code)      # for debugging

                query = '''DELETE FROM Матеріали WHERE Код_матеріалу=?;'''
                conn.execute(query, (code,) )

                msg = QMessageBox()
                msg.setWindowTitle("Результат виконання")
                msg.setWindowIcon(QIcon(u":/newPrefix/assets/success_icon.png"))
                msg.setText("Операція виконана успішно!")
                x = msg.exec_() 
                # self.tableWidget.removeRow(current_row)

        except sqlite3.Error as e:
            # print(e)              #for debugging
            # print(e.args)

            msg = QMessageBox()
            msg.setWindowTitle("Результат виконання")
            msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
            msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
            x = msg.exec_() 
            
        conn.commit()
        conn.close()
        self.load_data_func()

    def load_data_func(self):
        self.tableWidget.setRowCount(0)
        # print('Rows set to 0')   for debugging
        connection = sqlite3.connect("atelie.db")
        cur = connection.cursor()
        sqlquery = "SELECT * FROM Матеріали"
        tablerow = 0
        total_rows_count = 0

        for row in cur.execute(sqlquery):
            total_rows_count += 1

        self.tableWidget.setRowCount(total_rows_count)
        # print(f'rows set to {total_rows_count}')      for debugging

        for row in cur.execute(sqlquery):

                    # print(row)        for debugging
            self.tableWidget.setItem(tablerow,0,QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow,1,QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow,2,QTableWidgetItem(row[2]))
            tablerow += 1

        QTimer.singleShot(10000, self.load_data_func)
        # print('data loaded ')     for debugging

    def search_func(self):

        items = self.tableWidget.findItems(self.find_field.text(), Qt.MatchExactly)
        if items:
            self.tableWidget.selectRow(items[0].row())
        else:
            QMessageBox.information(self, 'Search Results', 'Нічого не знайдено. Спробуйте ще раз')
            
            
                    # print('err')        for debugging
        



    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(803, 459)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(760, 0, 41, 31))

        font = QFont()
        font.setPointSize(2)

        self.exit_button.setFont(font)

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit_button.setIcon(icon)
        self.exit_button.setIconSize(QSize(25, 25))

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 350, 111, 21))

        font1 = QFont()
        font1.setPointSize(13)
        self.label_2.setFont(font1)

        self.edit_button = QPushButton(self.centralwidget)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setGeometry(QRect(300, 350, 141, 31))

        font2 = QFont()
        font2.setPointSize(12)

        self.edit_button.setFont(font2)

        self.update_button = QPushButton(self.centralwidget)
        self.update_button.setObjectName(u"update_button")
        self.update_button.setGeometry(QRect(610, 350, 141, 31))
        self.update_button.setFont(font2)

        self.up_button = QPushButton(self.centralwidget)
        self.up_button.setObjectName(u"up_button")
        self.up_button.setGeometry(QRect(10, 150, 41, 41))
        self.up_button.setFont(font1)

        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/up_arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.up_button.setIcon(icon1)
        self.up_button.setIconSize(QSize(30, 30))

        self.find_field = QLineEdit(self.centralwidget)
        self.find_field.setObjectName(u"find_field")
        self.find_field.setGeometry(QRect(160, 350, 71, 21))

        font3 = QFont()
        font3.setPointSize(10)

        self.find_field.setFont(font3)

        self.delete_button = QPushButton(self.centralwidget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(450, 350, 141, 31))
        self.delete_button.setFont(font2)

        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(0, 0, 41, 31))
        self.back_button.setFont(font)

        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back_button.setIcon(icon2)
        self.back_button.setIconSize(QSize(25, 25))

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(80, 50, 671, 291))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnWidth(0,90)
        self.tableWidget.setColumnWidth(1,300)
        self.tableWidget.setColumnWidth(2,270)
        self.tableWidget.setHorizontalHeaderLabels(["Код матеріалу","Назва","Виробник"])
        self.tableWidget.verticalHeader().setVisible(False)
        

        self.load_data_func()

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 10, 121, 31))

        font4 = QFont()
        font4.setPointSize(17)
        self.label.setFont(font4)

        self.find_button = QPushButton(self.centralwidget)
        self.find_button.setObjectName(u"find_button")
        self.find_button.setGeometry(QRect(160, 380, 71, 31))
        self.find_button.setFont(font1)

        self.down_button = QPushButton(self.centralwidget)
        self.down_button.setObjectName(u"down_button")
        self.down_button.setGeometry(QRect(10, 190, 41, 41))

        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/assets/down_arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.down_button.setIcon(icon3)
        self.down_button.setIconSize(QSize(30, 30))

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Перегляд матеріалів", u"Перегляд матеріалів", None))
        self.exit_button.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u043c\u0430\u0442\u0435\u0440\u0456\u0430\u043b\u0443", None))
        self.edit_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043c\u0456\u043d\u0438\u0442\u0438", None))
        self.update_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043d\u043e\u0432\u0438\u0442\u0438 \u0442\u0430\u0431\u043b\u0438\u0446\u044e", None))
        self.up_button.setText("")
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0437\u0430\u043f\u0438\u0441", None))
        self.back_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0435\u0440\u0456\u0430\u043b\u0438", None))
        self.find_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0448\u0443\u043a", None))
        self.down_button.setText("")
    # retranslateUi

class edit_material(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.cancel_button.clicked.connect(self.to_materials_list_func)
        self.submit_button.clicked.connect(self.edit_func)
        self.code = None

    def set_code(self, code):
        self.code = code

    def edit_func(self):
        name = self.name_field.text()
        producer = self.producer_field.text()
        code = self.code

        #print('DATA = ',name,producer,code)   # for debugging
        
        if name == '' or producer == '':
            msg = QMessageBox()
            msg.setWindowTitle("Результат виконання")
            msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
            msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
            x = msg.exec_() 
        else:
            try:
                conn = sqlite3.connect("atelie.db") 
                with conn:

                    query = '''UPDATE Матеріали SET Назва = ?, Виробник = ? WHERE Код_матеріалу = ?;'''
                    conn.execute(query, (name,producer,code) )

                    msg = QMessageBox()
                    msg.setWindowTitle("Результат виконання")
                    msg.setWindowIcon(QIcon(u":/newPrefix/assets/success_icon.png"))
                    msg.setText("Операція виконана успішно!")
                    x = msg.exec_() 
                    # self.tableWidget.removeRow(current_row)

            except sqlite3.Error as e:
                # print(e)              #for debugging
                # print(e.args)

                msg = QMessageBox()
                msg.setWindowTitle("Результат виконання")
                msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
                msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
                x = msg.exec_() 
                
            conn.commit()
            conn.close()
            self.close()

    def to_materials_list_func(self):
        self.close()

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(567, 342)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.submit_button = QPushButton(self.centralwidget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(190, 270, 131, 31))

        font = QFont()
        font.setPointSize(13)

        self.submit_button.setFont(font)

        self.name_field = QLineEdit(self.centralwidget)
        self.name_field.setObjectName(u"name_field")
        self.name_field.setGeometry(QRect(150, 100, 341, 31))

        font1 = QFont()
        font1.setPointSize(11)

        self.name_field.setFont(font1)

        self.producer_field = QLineEdit(self.centralwidget)
        self.producer_field.setObjectName(u"producer_field")
        self.producer_field.setGeometry(QRect(150, 160, 341, 31))
        self.producer_field.setFont(font1)

        self.cancel_button = QPushButton(self.centralwidget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(340, 270, 131, 31))
        self.cancel_button.setFont(font)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 20, 221, 31))

        font2 = QFont()
        font2.setPointSize(17)

        self.label.setFont(font2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 131, 61))
        self.label_2.setFont(font)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 140, 101, 61))
        self.label_3.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Редагування запису", u"Редагування запису", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0456\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0438", None))
        self.producer_field.setInputMask("")
        self.cancel_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0438\u0442\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u043d\u043e\u0432\u0456 \u0434\u0430\u043d\u0456", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430 \u043c\u0430\u0442\u0435\u0440\u0456\u0430\u043b\u0443", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0440\u043e\u0431\u043d\u0438\u043a", None))
    # retranslateUi

class add_product(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.file_dialog_button.clicked.connect(self.file_dialog_func)
        self.submit_button.clicked.connect(self.add_func)
        self.exit_button.clicked.connect(exit_func)
        self.data = self.back_button.clicked.connect(self.to_services_func)

    def to_services_func(self):
        self.cams = services()
        self.cams.show()
        self.close()
    
    def file_dialog_func(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '',"JPEG (*.JPEG *.jpeg *.JPG *.jpg *.JPE *.jpe *JFIF *.jfif);; PNG (*.PNG *.png);; GIF (*.GIF *.gif);; Bitmap Files (*.BMP *.bmp *.DIB *.dib);; TIFF (*.TIF *.tif *.TIFF *.tiff);; ICO (*.ICO *.ico)")[0]
        f = open(fname, 'rb')
        

        with f:
            self.data = f.read()
            image_profile = QImage(fname) #QImage object
            image_profile = image_profile.scaled(191,191, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation) # To scale image for example and keep its Aspect Ration    
            self.photo_view.setPixmap(QPixmap.fromImage(image_profile)) 
            

    def add_func(self):
        conn = sqlite3.connect("atelie.db")

        try:
            with conn:
                
                list_item = self.material_list.currentText()
                cur = conn.cursor()
                row = cur.execute('SELECT Код_матеріалу FROM Матеріали WHERE Назва =?',(str(list_item),))
                material = row.fetchall()[0][0]

        except sqlite3.Error as e:
            print(e)
            print(e.args)
        
        name = self.name_field.text()
        type_of_prod = self.type_field.text()
        type = 'Пошив одягу'
        color = self.color_field.text()
        price = self.price_field.text()

        if name == '' or type_of_prod == '' or color == '' or price == '' or self.data == True:
            msg = QMessageBox()
            msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
            msg.setWindowTitle("Результат виконання")
            msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
            x = msg.exec_() 
        else:

            try:
                with conn:
                    row = (type,type_of_prod,name,material,color,self.data,price)
                    # print('DATA =', row)      # for debugging
        
                    query = '''insert into Послуги (Тип_послуги, Тип_продукту, Назва, Код_матеріалу, Колір, Фото_продукту, Вартість)
                                values (?, ?, ?, ?, ?, ?, ?);'''
                    conn.execute(query, row)

                    self.name_field.clear()
                    self.type_field.clear()
                    self.color_field.clear()
                    self.price_field.clear()
                    self.photo_view.clear()
                    
                    

                    msg = QMessageBox()
                    msg.setWindowIcon(QIcon(u":/newPrefix/assets/success_icon.png"))
                    msg.setWindowTitle("Результат виконання")
                    msg.setText("Операція виконана успішно!")
                    x = msg.exec_() 

            except sqlite3.Error as e:
                print(e)              #for debugging
                print(e.args)

                
                msg = QMessageBox()
                msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
                msg.setWindowTitle("Результат виконання")
                msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
                x = msg.exec_() 

            conn.commit()
            conn.close()


    
    def load_data_func(self):
        conn = sqlite3.connect("atelie.db") 

        try:
            with conn:
                
                query = '''SELECT Назва FROM Матеріали;'''
                cur = conn.cursor()
                tablerow = 0
                
                for row in cur.execute(query):

                    self.material_list.insertItem(tablerow,row[0])
                    tablerow += 1
            conn.close()

        except sqlite3.Error as e:
            # print(e)              for debugging
            # print(e.args)

            conn.close()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(871, 499)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(830, 0, 41, 31))

        font = QFont()
        font.setPointSize(2)

        self.exit_button.setFont(font)

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit_button.setIcon(icon)
        self.exit_button.setIconSize(QSize(25, 25))

        self.type_field = QLineEdit(self.centralwidget)
        self.type_field.setObjectName(u"type_field")
        self.type_field.setGeometry(QRect(190, 180, 261, 31))

        font1 = QFont()
        font1.setPointSize(12)

        self.type_field.setFont(font1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(360, 0, 171, 41))

        font2 = QFont()
        font2.setPointSize(16)

        self.label_3.setFont(font2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 140, 171, 31))

        font3 = QFont()
        font3.setPointSize(11)

        self.label.setFont(font3)
        
        self.name_field = QLineEdit(self.centralwidget)
        self.name_field.setObjectName(u"name_field")
        self.name_field.setGeometry(QRect(190, 140, 261, 31))
        self.name_field.setFont(font1)

        self.submit_button = QPushButton(self.centralwidget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(710, 420, 101, 31))
        self.submit_button.setFont(font3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 180, 161, 31))
        self.label_2.setFont(font3)

        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(0, 0, 41, 31))
        self.back_button.setFont(font)

        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back_button.setIcon(icon1)
        self.back_button.setIconSize(QSize(25, 25))

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 220, 161, 31))
        self.label_4.setFont(font3)

        self.material_list = QComboBox(self.centralwidget)
        self.material_list.setObjectName(u"material_list")
        self.material_list.setGeometry(QRect(190, 230, 261, 21))
        self.material_list.setFont(font1)

        self.load_data_func()

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(470, 140, 191, 31))
        self.label_5.setFont(font3)

        self.color_field = QLineEdit(self.centralwidget)
        self.color_field.setObjectName(u"color_field")
        self.color_field.setGeometry(QRect(660, 140, 171, 31))
        self.color_field.setFont(font1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(470, 180, 191, 31))
        self.label_6.setFont(font3)

        self.price_field = QLineEdit(self.centralwidget)
        self.price_field.setObjectName(u"price_field")
        self.price_field.setGeometry(QRect(660, 180, 171, 31))
        self.price_field.setFont(font1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 280, 171, 31))
        self.label_7.setFont(font3)

        self.file_dialog_button = QPushButton(self.centralwidget)
        self.file_dialog_button.setObjectName(u"file_dialog_button")
        self.file_dialog_button.setGeometry(QRect(400, 280, 111, 31))
        self.file_dialog_button.setFont(font3)

        self.photo_view = QLabel(self.centralwidget)
        self.photo_view.setObjectName(u"photo_view")
        self.photo_view.setGeometry(QRect(200, 290, 191, 191))
        self.photo_view.setFrameShadow(QFrame.Plain)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.exit_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043f\u0440\u043e\u0434\u0443\u043a\u0442", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u043d\u0430\u0437\u0432\u0443 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0443", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0442\u0438\u043f \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0443", None))
        self.back_button.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0435\u0440\u0456\u0442\u044c \u043c\u0430\u0442\u0435\u0440\u0456\u0430\u043b", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u043a\u043e\u043b\u0456\u0440 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0443", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0432\u0430\u0440\u0442\u0456\u0441\u0442\u044c \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0443", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0439\u0442\u0435 \u0444\u043e\u0442\u043e \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0443", None))
        self.file_dialog_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0440\u0430\u0442\u0438 \u0444\u043e\u0442\u043e", None))
        self.photo_view.setText("")
    # retranslateUi

class products_list(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.back_button.clicked.connect(self.to_services_func)
        self.exit_button.clicked.connect(exit_func)
        self.up_button.clicked.connect(self.previous_item_func)
        self.down_button.clicked.connect(self.next_item_func)
        self.find_button.clicked.connect(self.search_func)
        self.delete_button.clicked.connect(self.delete_func)
        self.update_button.clicked.connect(self.load_data_func)
        self.tableWidget.clicked.connect(self.currention_func)
        self.edit_button.clicked.connect(self.edit_func)
        self.tableWidget.doubleClicked.connect(self.show_image_func)


    def show_image_func(self):
        self.code = self.tableWidget.item(self.tableWidget.currentRow(),0).text()
        self.popup = photo_viewing(code=self.code)
        self.popup.show()

    def to_services_func(self):
        self.cams = services()
        self.cams.show()
        self.close()
    
    def previous_item_func(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow()-1)
    
    def next_item_func(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow()+1)

    def currention_func(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow())

    def search_func(self):
        items = self.tableWidget.findItems(self.find_field.text(), Qt.MatchExactly)
        if items:
            self.tableWidget.selectRow(items[0].row())
        else:
            QMessageBox.information(self, 'Search Results', 'Нічого не знайдено. Спробуйте ще раз')

    def delete_func(self):
        code = self.tableWidget.item(self.tableWidget.currentRow(),self.tableWidget.currentColumn()).text()
        conn = sqlite3.connect("atelie.db") 

        try:
            with conn:
                
                # print('DATA =', code)      # for debugging

                query = '''DELETE FROM Послуги WHERE Код_продукту=?;'''
                conn.execute(query, (code,) )

                msg = QMessageBox()
                msg.setWindowTitle("Результат виконання")
                msg.setWindowIcon(QIcon(u":/newPrefix/assets/success_icon.png"))
                msg.setText("Операція виконана успішно!")
                x = msg.exec_() 
                # self.tableWidget.removeRow(current_row)

        except sqlite3.Error as e:
            # print(e)              #for debugging
            # print(e.args)

            msg = QMessageBox()
            msg.setWindowTitle("Результат виконання")
            msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
            msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
            x = msg.exec_() 
            
        conn.commit()
        conn.close()
        self.load_data_func()

    def load_data_func(self):
        self.tableWidget.setRowCount(0)
        # print('Rows set to 0')   for debugging
        connection = sqlite3.connect("atelie.db")
        cur = connection.cursor()
        sqlquery = "SELECT Код_продукту, Тип_продукту, Назва, Код_матеріалу, Колір, Фото_продукту, Вартість FROM Послуги WHERE Код_матеріалу IS NOT NULL;"
        tablerow = 0
        total_rows_count = 0

        for row in cur.execute(sqlquery):
            total_rows_count += 1

        self.tableWidget.setRowCount(total_rows_count)
        # print(f'rows set to {total_rows_count}')      for debugging
        
        for row in cur.execute(sqlquery):
            
                    # print(row)        for debugging
            self.tableWidget.setItem(tablerow,0,QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(tablerow,1,QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tablerow,2,QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(tablerow,3,QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow,4,QTableWidgetItem(str(row[4])))

            image_profile = QImage(u":/newPrefix/assets/screpka.png") #QImage object
            image_profile = image_profile.scaled(15,20, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation) # To scale image for example and keep its Aspect Ration    

            self.pic_label = QLabel()
            self.pic_label.setPixmap(QPixmap.fromImage(image_profile))
            self.tableWidget.setCellWidget(tablerow, 5, self.pic_label)

            self.tableWidget.setItem(tablerow,6,QTableWidgetItem(str(row[6])+' ₴'))
            

            tablerow += 1
        QTimer.singleShot(10000, self.load_data_func)
        # print('data loaded ')     for debugging

    def edit_func(self):
        code = self.tableWidget.item(self.tableWidget.currentRow(),self.tableWidget.currentColumn()).text()
        self.cams = edit_product(code)
        self.cams.show()


    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(803, 449)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.delete_button = QPushButton(self.centralwidget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(450, 350, 141, 31))

        font = QFont()
        font.setPointSize(12)

        self.delete_button.setFont(font)

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(760, 0, 41, 31))

        font1 = QFont()
        font1.setPointSize(2)

        self.exit_button.setFont(font1)

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit_button.setIcon(icon)
        self.exit_button.setIconSize(QSize(25, 25))

        self.update_button = QPushButton(self.centralwidget)
        self.update_button.setObjectName(u"update_button")
        self.update_button.setGeometry(QRect(610, 350, 141, 31))
        self.update_button.setFont(font)

        self.up_button = QPushButton(self.centralwidget)
        self.up_button.setObjectName(u"up_button")
        self.up_button.setGeometry(QRect(10, 150, 41, 41))

        font2 = QFont()
        font2.setPointSize(13)

        self.up_button.setFont(font2)

        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/up_arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.up_button.setIcon(icon1)
        self.up_button.setIconSize(QSize(30, 30))

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 360, 111, 21))
        self.label_2.setFont(font2)

        self.down_button = QPushButton(self.centralwidget)
        self.down_button.setObjectName(u"down_button")
        self.down_button.setGeometry(QRect(10, 190, 41, 41))

        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/assets/down_arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.down_button.setIcon(icon2)
        self.down_button.setIconSize(QSize(30, 30))

        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(0, 0, 41, 31))
        self.back_button.setFont(font1)

        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back_button.setIcon(icon3)
        self.back_button.setIconSize(QSize(25, 25))

        self.find_field = QLineEdit(self.centralwidget)
        self.find_field.setObjectName(u"find_field")
        self.find_field.setGeometry(QRect(170, 360, 71, 21))

        font3 = QFont()
        font3.setPointSize(10)

        self.find_field.setFont(font3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 10, 111, 31))

        font4 = QFont()
        font4.setPointSize(17)

        self.label.setFont(font4)

        self.tableWidget = QTableWidget(self.centralwidget)

        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)

        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(70, 50, 701, 291))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setColumnWidth(4,70)
        self.tableWidget.setColumnWidth(0,85)
        self.tableWidget.setColumnWidth(1,150)
        self.tableWidget.setColumnWidth(2,150)
        self.tableWidget.setColumnWidth(5,40)
        self.tableWidget.setHorizontalHeaderLabels(["Код продукту","Тип продукту","Назва","Код матеріалу","Колір",'Фото','Вартість'])
        self.tableWidget.verticalHeader().setVisible(False)
        
        self.load_data_func()

        self.edit_button = QPushButton(self.centralwidget)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setGeometry(QRect(300, 350, 141, 31))
        self.edit_button.setFont(font)

        self.find_button = QPushButton(self.centralwidget)
        self.find_button.setObjectName(u"find_button")
        self.find_button.setGeometry(QRect(170, 390, 71, 31))
        self.find_button.setFont(font2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Перегляд продуктів", u"Перегляд продуктів", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0437\u0430\u043f\u0438\u0441", None))
        self.exit_button.setText("")
        self.update_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043d\u043e\u0432\u0438\u0442\u0438 \u0442\u0430\u0431\u043b\u0438\u0446\u044e", None))
        self.up_button.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0434 \u0432\u0438\u0440\u043e\u0431\u0443", None))
        self.down_button.setText("")
        self.back_button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0440\u043e\u0431\u0438", None))
        self.edit_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043c\u0456\u043d\u0438\u0442\u0438", None))
        self.find_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0448\u0443\u043a", None))
    # retranslateUi

class photo_viewing(QMainWindow):

    def __init__(self,code):
        super().__init__()
        self.code = code
        self.setupUi(self,self.code)
        
        
        self.back_button.clicked.connect(self.to_products_list_func)
        

    def to_products_list_func(self):
        self.close()
        
    
    def load_photo_func(self,code):
        try:
            conn = sqlite3.connect("atelie.db") 
            with conn:

                query = '''SELECT Фото_продукту FROM Послуги WHERE Код_продукту=?;'''
                cur = conn.cursor()
                
                row = cur.execute(query, code)
                row = row.fetchall()[0][0]
                image_profile = QPixmap() #QImage object
                image_profile.loadFromData(row)
                image_profile = image_profile.scaled(371,371, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation) # To scale image for example and keep its Aspect Ration    
                self.picture.setPixmap(image_profile)

        except sqlite3.Error as e:
            print(e)              #for debugging
            print(e.args)

            msg = QMessageBox()
            msg.setWindowTitle("Результат виконання")
            msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
            msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
            x = msg.exec_() 

    def setupUi(self, MainWindow, code):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.picture = QLabel(self.centralwidget)
        self.picture.setObjectName(u"picture")
        self.picture.setGeometry(QRect(90, 30, 371, 371))
        
        self.load_photo_func(code)
        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(0, 0, 41, 31))
        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QSize(25, 25))
        self.back_button.setCheckable(False)
        self.back_button.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Перегляд фото", u"Перегляд фото", None))
        self.picture.setText("")
        self.back_button.setText("")
    # retranslateUi

class edit_product(QMainWindow):
    def __init__(self,code):
        super().__init__()
        self.code = code
        self.setupUi(self)
        
        self.file_dialog_button.clicked.connect(self.file_dialog_func)
        self.back_button.clicked.connect(self.to_products_list_func)
        self.submit_button.clicked.connect(self.edit_func)
        
    def file_dialog_func(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '',"JPEG (*.JPEG *.jpeg *.JPG *.jpg *.JPE *.jpe *JFIF *.jfif);; PNG (*.PNG *.png);; GIF (*.GIF *.gif);; Bitmap Files (*.BMP *.bmp *.DIB *.dib);; TIFF (*.TIF *.tif *.TIFF *.tiff);; ICO (*.ICO *.ico)")[0]
        f = open(fname, 'rb')
        

        with f:
            self.data = f.read()
            image_profile = QImage(fname) #QImage object
            image_profile = image_profile.scaled(191,191, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation) # To scale image for example and keep its Aspect Ration    
            self.photo_view.setPixmap(QPixmap.fromImage(image_profile)) 

    def edit_func(self):
        conn = sqlite3.connect("atelie.db")

        try:
            with conn:
                
                list_item = self.material_list.currentText()
                cur = conn.cursor()
                row = cur.execute('SELECT Код_матеріалу FROM Матеріали WHERE Назва =?',(str(list_item),))
                material = row.fetchall()[0][0]

        except sqlite3.Error as e:
            print(e)
            print(e.args)
        
        name = self.name_field.text()
        type_of_prod = self.type_field.text()
        type = 'Пошив одягу'
        color = self.color_field.text()
        price = self.price_field.text()

        if name == '' or type_of_prod == '' or color == '' or price == '' or self.data == True:
            msg = QMessageBox()
            msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
            msg.setWindowTitle("Результат виконання")
            msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
            x = msg.exec_() 
        else:

            try:
                with conn:
                    row = (type,type_of_prod,name,material,color,self.data,price,self.code)
                    # print('DATA =', row)      # for debugging
        
                    query = '''UPDATE Послуги SET Тип_послуги=?, Тип_продукту=?, Назва=?, Код_матеріалу=?, Колір=?, Фото_продукту=?, Вартість=? WHERE Код_продукту=?;'''
                    conn.execute(query, row)

                    self.name_field.clear()
                    self.type_field.clear()
                    self.color_field.clear()
                    self.price_field.clear()
                    self.photo_view.clear()
                    

                    msg = QMessageBox()
                    msg.setWindowIcon(QIcon(u":/newPrefix/assets/success_icon.png"))
                    msg.setWindowTitle("Результат виконання")
                    msg.setText("Операція виконана успішно!")
                    x = msg.exec_() 

            except sqlite3.Error as e:
                print(e)              #for debugging
                print(e.args)

                
                msg = QMessageBox()
                msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
                msg.setWindowTitle("Результат виконання")
                msg.setText("Виникла помилка, перевірте правильність данних та заповненість всіх полей")
                x = msg.exec_() 

            conn.commit()
            conn.close()

    def load_data_func(self):
        conn = sqlite3.connect("atelie.db") 

        try:
            with conn:
                
                query = '''SELECT Назва FROM Матеріали;'''
                cur = conn.cursor()
                tablerow = 0
                
                for row in cur.execute(query):

                    self.material_list.insertItem(tablerow,row[0])
                    tablerow += 1
            conn.close()

        except sqlite3.Error as e:
            # print(e)              for debugging
            # print(e.args)

            conn.close()

    def to_products_list_func(self):
        self.close()

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(848, 500)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.type_field = QLineEdit(self.centralwidget)
        self.type_field.setObjectName(u"type_field")
        self.type_field.setGeometry(QRect(190, 180, 261, 31))

        font = QFont()
        font.setPointSize(12)

        self.type_field.setFont(font)

        self.name_field = QLineEdit(self.centralwidget)
        self.name_field.setObjectName(u"name_field")
        self.name_field.setGeometry(QRect(190, 140, 261, 31))
        self.name_field.setFont(font)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 220, 161, 31))

        font1 = QFont()
        font1.setPointSize(11)

        self.label_4.setFont(font1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 280, 171, 31))
        self.label_7.setFont(font1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 180, 161, 31))
        self.label_2.setFont(font1)

        self.material_list = QComboBox(self.centralwidget)
        self.material_list.addItem("")
        self.material_list.addItem("")
        self.material_list.addItem("")
        self.material_list.setObjectName(u"material_list")
        self.material_list.setGeometry(QRect(190, 230, 261, 21))
        self.material_list.setFont(font)
        self.load_data_func()

        self.color_field = QLineEdit(self.centralwidget)
        self.color_field.setObjectName(u"color_field")
        self.color_field.setGeometry(QRect(660, 140, 171, 31))
        self.color_field.setFont(font)

        self.submit_button = QPushButton(self.centralwidget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setGeometry(QRect(710, 420, 101, 31))
        self.submit_button.setFont(font1)

        self.photo_view = QLabel(self.centralwidget)
        self.photo_view.setObjectName(u"photo_view")
        self.photo_view.setGeometry(QRect(200, 290, 191, 191))
        self.photo_view.setFrameShadow(QFrame.Plain)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(470, 180, 191, 31))
        self.label_6.setFont(font1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(330, 10, 171, 41))

        font2 = QFont()
        font2.setPointSize(16)

        self.label_3.setFont(font2)

        self.price_field = QLineEdit(self.centralwidget)
        self.price_field.setObjectName(u"price_field")
        self.price_field.setGeometry(QRect(660, 180, 171, 31))
        self.price_field.setFont(font)

        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(0, 0, 41, 31))

        font3 = QFont()
        font3.setPointSize(2)

        self.back_button.setFont(font3)

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QSize(25, 25))

        self.file_dialog_button = QPushButton(self.centralwidget)
        self.file_dialog_button.setObjectName(u"file_dialog_button")
        self.file_dialog_button.setGeometry(QRect(400, 280, 111, 31))
        self.file_dialog_button.setFont(font1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 140, 171, 31))
        self.label.setFont(font1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(470, 140, 191, 31))
        self.label_5.setFont(font1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Редагування", u"Редагування", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0435\u0440\u0456\u0442\u044c \u043c\u0430\u0442\u0435\u0440\u0456\u0430\u043b", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0439\u0442\u0435 \u0444\u043e\u0442\u043e \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0443", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0442\u0438\u043f \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0443", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0456\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0438", None))
        self.photo_view.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u0432\u0430\u0440\u0442\u0456\u0441\u0442\u044c \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0443", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u043d\u043e\u0432\u0456 \u0434\u0430\u043d\u0456", None))
        self.back_button.setText("")
        self.file_dialog_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0431\u0440\u0430\u0442\u0438 \u0444\u043e\u0442\u043e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u043d\u0430\u0437\u0432\u0443 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0443", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0456\u0442\u044c \u043a\u043e\u043b\u0456\u0440 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0443", None))
    # retranslateUi




if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = start()
    widget.show()
    

    try:
        sys.exit(app.exec_())
    except:
        print('exiting..')




        """"""