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

def exitfunc():
    print('exiting...')
    sys.exit()


# Стартовое меню
class start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.to_main_menu_func)
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

        self.setWindowIcon(QIcon(u":/newPrefix/assets/start_menu_icon.png"))

        self.tostart.clicked.connect(self.tostartfunc)
        self.exit.clicked.connect(exitfunc)
        self.clients.clicked.connect(self.toclientsfunc)
        self.workers.clicked.connect(self.toworkersfunc)
    
    def toworkersfunc(self):
        self.cams = workers()
        self.cams.show()
        self.close()

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

        self.setWindowIcon(QIcon(u":/newPrefix/assets/clients_icon.png"))

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

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 0, 111, 31))
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)

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

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0456\u0454\u043d\u0442\u0438", None))
        self.add_new_client.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043d\u043e\u0432\u043e\u0433\u043e \u043a\u043b\u0456\u0454\u043d\u0442\u0430", None))
        self.view_clients.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0433\u043b\u044f\u0434 \u043a\u043b\u0456\u0454\u043d\u0442\u0456\u0432", None))
        self.clients_zvit.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0432\u0456\u0442\u043d\u0456\u0441\u0442\u044c \u043f\u043e \u043a\u043b\u0456\u0454\u0442\u0430\u043c", None))
        self.back.setText("")
        self.exit.setText("")
    # retranslateUi

# Добавить клиента
class add_client(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon(u":/newPrefix/assets/plus_icon.png"))
        self.back.clicked.connect(self.to_clients)
        self.exit.clicked.connect(exitfunc)
        self.submit_addittion.clicked.connect(self.addclient)
        self.phone.setInputMask('999-999')

    def addclient(self):
        conn = sqlite3.connect("atelie.db") 
        name = self.name.text()
        phone = self.phone.text()
        print(phone)
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

                    self.name.clear()
                    self.phone.clear()

                    msg = QMessageBox()
                    msg.setWindowIcon(QIcon(u":/newPrefix/assets/success_icon.png"))
                    msg.setWindowTitle("Результат виконання")
                    msg.setText("Операція виконана успішно!")
                    x = msg.exec_() 

            except sqlite3.Error as e:
                # print(e)              for debugging
                # print(e.args)

                self.name.clear()
                self.phone.clear()

                msg = QMessageBox()
                msg.setWindowIcon(QIcon(u":/newPrefix/assets/error_icon.png"))
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
        
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 0, 201, 41))
        font3 = QFont()
        font3.setPointSize(16)
        self.label_3.setFont(font3)

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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043a\u043b\u0456\u0454\u043d\u0442\u0430", None))
    # retranslateUi

# Просмотр клиентов
class clients_list(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

        self.setWindowIcon(QIcon(u":/newPrefix/assets/list_icon.png"))

        self.back.clicked.connect(self.to_clients)
        self.exit.clicked.connect(exitfunc)
        self.downbutton.clicked.connect(self.next_item)
        self.upbutton.clicked.connect(self.previous_item)
        self.findbutton.clicked.connect(self.searchfunc)
        self.update2.clicked.connect(self.load_data)
        self.delete_2.clicked.connect(self.deletefunc)
        self.tableWidget.clicked.connect(self.currentionfunc)
        self.edit_button.clicked.connect(self.editfunc)

    def editfunc(self):

        code = self.tableWidget.item(self.tableWidget.currentRow(),self.tableWidget.currentColumn()).text()
        self.cams = edit_client()
        self.cams.set_code(code=code)
        self.cams.show()
        
    def currentionfunc(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow())

    def next_item(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow()+1)
        
    def previous_item(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow()-1)

    def deletefunc(self):
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
        self.load_data()

    def to_clients(self):
        self.cams = clients()
        self.cams.show()
        self.close()  
        
    def load_data(self):
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
        QTimer.singleShot(10000, self.load_data)
        # print('data loaded ')     for debugging

    def searchfunc(self):

        items = self.tableWidget.findItems(self.find_edit.text(), Qt.MatchExactly)
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

        self.load_data()

        self.delete_2 = QPushButton(self.centralwidget)
        self.delete_2.setObjectName(u"delete_2")
        self.delete_2.setGeometry(QRect(450, 350, 141, 31))

        font4 = QFont()
        font4.setPointSize(12)

        self.delete_2.setFont(font4)

        self.update2 = QPushButton(self.centralwidget)
        self.update2.setObjectName(u"update")
        self.update2.setGeometry(QRect(610, 350, 141, 31))
        self.update2.setFont(font4)

        self.edit_button = QPushButton(self.centralwidget)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setGeometry(QRect(300, 350, 141, 31))
        self.edit_button.setFont(font4)

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
        self.delete_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0437\u0430\u043f\u0438\u0441", None))
        self.update2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043d\u043e\u0432\u0438\u0442\u0438 \u0442\u0430\u0431\u043b\u0438\u0446\u044e", None))
        self.edit_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043c\u0456\u043d\u0438\u0442\u0438", None))
    # retranslateUi

# Меню работников
class workers(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.to_mainmenu)
        self.exit.clicked.connect(exitfunc)
        self.view_workers.clicked.connect(self.to_workerslist)
        self.add_new_worker.clicked.connect(self.to_add_workerfunc)

    def to_add_workerfunc(self):
        self.cams = add_workers()
        self.cams.show()
        self.close()

    def to_workerslist(self):
        self.cams = workers_list()
        self.cams.show()
        self.close()

    def to_mainmenu(self):
        self.cams = main_menu()
        self.cams.show()
        self.close()

    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(830, 299)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.add_new_worker = QPushButton(self.centralwidget)
        self.add_new_worker.setObjectName(u"add_new_worker")
        self.add_new_worker.setGeometry(QRect(50, 140, 161, 31))

        self.workers_analisys = QPushButton(self.centralwidget)
        self.workers_analisys.setObjectName(u"workers_analisys")
        self.workers_analisys.setGeometry(QRect(610, 140, 161, 31))

        self.view_workers = QPushButton(self.centralwidget)
        self.view_workers.setObjectName(u"view_workers")
        self.view_workers.setGeometry(QRect(320, 140, 161, 31))

        self.exit = QPushButton(self.centralwidget)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(790, 0, 41, 31))

        icon = QIcon()
        icon.addFile(u":/newPrefix/assets/exit.png", QSize(), QIcon.Normal, QIcon.Off)

        self.exit.setIcon(icon)
        self.exit.setIconSize(QSize(25, 25))
        self.exit.setCheckable(False)
        self.exit.setFlat(False)

        self.back = QPushButton(self.centralwidget)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(0, 0, 41, 31))

        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/assets/arrow.png", QSize(), QIcon.Normal, QIcon.Off)

        self.back.setIcon(icon1)
        self.back.setIconSize(QSize(25, 25))
        self.back.setCheckable(False)
        self.back.setFlat(False)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(360, 0, 111, 31))

        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)

        self.label.setFont(font)

        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Працівники", u"Працівники", None))
        self.add_new_worker.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0434\u0430\u0442\u0438 \u043d\u043e\u0432\u043e\u0433\u043e \u043f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0430", None))
        self.workers_analisys.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0456\u0437 \u043f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0456\u0432", None))
        self.view_workers.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0433\u043b\u044f\u0434 \u043f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0456\u0432", None))
        self.exit.setText("")
        self.back.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0446\u0456\u0432\u043d\u0438\u043a\u0438", None))
    # retranslateUi

# Просмотр работников
class workers_list(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(u":/newPrefix/assets/list_icon.png"))

        self.back_button.clicked.connect(self.to_workersfunc)
        self.exit_button.clicked.connect(exitfunc)
        self.up_button.clicked.connect(self.previous_item)
        self.down_button.clicked.connect(self.next_item)
        self.find_button.clicked.connect(self.searchfunc)
        self.delete_button.clicked.connect(self.deletefunc)
        self.update_button.clicked.connect(self.load_data)
        self.tableWidget.clicked.connect(self.currentionfunc)

    def currentionfunc(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow())

    def next_item(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow()+1)
        
    def previous_item(self):
        self.tableWidget.selectRow(self.tableWidget.currentRow()-1)

    def searchfunc(self):
        items = self.tableWidget.findItems(self.find_edit.text(), Qt.MatchExactly)
        if items:
            self.tableWidget.selectRow(items[0].row())
        else:
            QMessageBox.information(self, 'Search Results', 'Нічого не знайдено. Спробуйте ще раз')
            # print('err')        for debugging
                    

    def deletefunc(self):
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

    def load_data(self):
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
        # print('data loaded ')     for debugging


    def to_workersfunc(self):
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

        self.load_data()

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
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(370, 350, 141, 31))

        font3 = QFont()
        font3.setPointSize(12)

        self.delete_button.setFont(font3)

        self.update_button = QPushButton(self.centralwidget)
        self.update_button.setObjectName(u"update_button")
        self.update_button.setGeometry(QRect(610, 350, 141, 31))
        self.update_button.setFont(font3)

        self.find_edit = QLineEdit(self.centralwidget)
        self.find_edit.setObjectName(u"find_edit")
        self.find_edit.setGeometry(QRect(210, 350, 71, 21))
        
        font4 = QFont()
        font4.setPointSize(10)
        self.find_edit.setFont(font4)

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(760, 0, 41, 31))
        self.exit_button.setFont(font2)
    
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
    # retranslateUi

class add_workers(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(u":/newPrefix/assets/plus_icon.png"))

        self.back_button.clicked.connect(self.to_workersfunc)
        self.exit_button.clicked.connect(exitfunc)
        self.submit_button.clicked.connect(self.add_workerfunc)
        self.phone.setInputMask('999-999')
        self.phone.setMaxLength(7)

            
                
    def to_workersfunc(self):
        self.cams = workers()
        self.cams.show()
        self.close()

    def add_workerfunc(self):
        
        conn = sqlite3.connect("atelie.db") 
        name = self.name.text()
        stazh = self.stazh.text()
        sex = self.sex.text()
        salary = self.salary.text()
        phone = self.phone.text()

        try:
            with conn:
                row = (name, stazh, phone, sex, salary)
                print('DATA =', row)      # for debugging

                query = '''insert into Працівники (ПІБ_працівника, Стаж, Телефон, Стать, Зарплата)
                            values (?, ?, ?, ?, ?);'''
                conn.execute(query, row)

                self.name.clear()
                self.phone.clear()
                self.stazh.clear()
                self.sex.clear()
                self.salary.clear()

                msg = QMessageBox()
                msg.setWindowIcon(QIcon(u":/newPrefix/assets/success_icon.png"))
                msg.setWindowTitle("Результат виконання")
                msg.setText("Операція виконана успішно!")
                x = msg.exec_() 

        except sqlite3.Error as e:
            # print(e)              for debugging
            # print(e.args)

            self.name.clear()
            self.phone.clear()

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

        self.stazh = QLineEdit(self.centralwidget)
        self.stazh.setObjectName(u"stazh")
        self.stazh.setGeometry(QRect(230, 160, 261, 31))

        font = QFont()
        font.setPointSize(12)

        self.stazh.setFont(font)

        self.name = QLineEdit(self.centralwidget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(230, 100, 261, 41))
        self.name.setFont(font)

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

        self.phone = QLineEdit(self.centralwidget)
        self.phone.setObjectName(u"phone")
        self.phone.setGeometry(QRect(230, 210, 261, 31))
        self.phone.setFont(font)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 260, 201, 31))
        self.label_5.setFont(font1)

        self.sex = QLineEdit(self.centralwidget)
        self.sex.setObjectName(u"sex")
        self.sex.setGeometry(QRect(230, 260, 261, 31))
        self.sex.setFont(font)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 320, 201, 31))
        self.label_6.setFont(font1)

        self.salary = QLineEdit(self.centralwidget)
        self.salary.setObjectName(u"salary")
        self.salary.setGeometry(QRect(230, 320, 261, 31))
        self.salary.setFont(font)

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
        name = self.lineEdit.text()
        phone = self.lineEdit_2.text()
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
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(140, 90, 341, 31))
        font2 = QFont()
        font2.setPointSize(11)
        self.lineEdit.setFont(font2)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(140, 150, 341, 31))
        self.lineEdit_2.setFont(font2)
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
        self.lineEdit_2.setInputMask(QCoreApplication.translate("MainWindow", u"999-999", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0456\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u0438", None))
        self.cancel_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0456\u0434\u043c\u0456\u043d\u0438\u0442\u0438", None))
    # retranslateUi


if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = start()
    widget.show()
    

    try:
        sys.exit(app.exec_())
    except:
        print('exiting..')