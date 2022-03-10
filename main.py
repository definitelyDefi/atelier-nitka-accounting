import sqlite3

import sys




from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,

)


class Contacts(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Main menu")
        self.resize(1280, 720)

        # Set up the view and load the data
        self.view = QTableWidget()
        
        self.view.setColumnCount(4)
        self.view.setHorizontalHeaderLabels(["ID", "Name", "Job", "Email"])
        
        query = QSqlQuery("SELECT id, name, job, email FROM contacts")

        while query.next():
            rows = self.view.rowCount()
            self.view.setRowCount(rows + 1)
            self.view.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))
            self.view.setItem(rows, 1, QTableWidgetItem(query.value(1)))
            self.view.setItem(rows, 2, QTableWidgetItem(query.value(2)))
            self.view.setItem(rows, 3, QTableWidgetItem(query.value(3)))

        self.view.resizeColumnsToContents()
        self.setCentralWidget(self.view)
        self.centerLayout = QVBoxLayout()
        self.centerLayout.addWidget(self.view, alignment=Qt.AlignCenter)



def set_connection(db_name):
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName(db_name)
    if not con.open():
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % con.lastError().databaseText(),
        )

        return False
    
    return con

def init_database(con):

    createTableQuery = QSqlQuery()
    createTableQuery.exec(

    """
    CREATE TABLE contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        name VARCHAR(40) NOT NULL,
        job VARCHAR(50),
        email VARCHAR(40) NOT NULL
    )

    """

    )
    print(con.tables())

    insertDataQuery = QSqlQuery()
    insertDataQuery.prepare(

    """
    INSERT INTO contacts (
        name,
        job,
        email
    )
    VALUES (?, ?, ?)
    """
    )
    data = [
    ("da", "Senior Web Developer", "joe@example.com"),
    ("Lara", "Project Manager", "lara@example.com"),
    ("David", "Data Analyst", "david@example.com"),
    ("Jane", "Senior Python Developer", "jane@example.com"),
    ]

# Use .addBindValue() to insert data

    for name, job, email in data:
        insertDataQuery.addBindValue(name)
        insertDataQuery.addBindValue(job)
        insertDataQuery.addBindValue(email)
        insertDataQuery.exec()



app = QApplication(sys.argv)
con = set_connection("atelie.db")
init_database(con)


win = Contacts()
win.show()
sys.exit(app.exec_())