from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import sqlite3
import sys
# connect to database
conn = sqlite3.connect('todo.db')
# enable data manipulation
cur = conn.cursor()
# create todo_list table
cur.execute('CREATE TABLE if not exists todo_list(list_item text)')
# commit new changes
conn.commit()
# close connection
conn.close()
class To_Do(object):
    def setupUi(self, MainWindow):
        # set properties for main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 339)
        # create central widget area on main window
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        # create entry (lineEdit), buttons and list widget
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.add_item_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_item())
        self.save_all_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.save_all_items())
        self.delete_item_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.delete_item())
        self.clear_items_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear_item())
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        # set object properties of widgets
        self.lineEdit.setObjectName("lineEdit")
        self.add_item_pushButton.setObjectName("add_item_pushButton")
        self.save_all_pushButton.setObjectName("save_all_pushButton")
        self.delete_item_pushButton.setObjectName("delete_item_pushButton")
        self.clear_items_pushButton.setObjectName("clear_items_pushButton")
        self.listWidget.setObjectName("listWidget")
        # set widgets geometry 
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 470, 31))
        self.add_item_pushButton.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.save_all_pushButton.setGeometry(QtCore.QRect(130, 50, 111, 31))
        self.delete_item_pushButton.setGeometry(QtCore.QRect(250, 50, 111, 31))
        self.clear_items_pushButton.setGeometry(QtCore.QRect(370, 50, 111, 31))
        self.listWidget.setGeometry(QtCore.QRect(10, 90, 470, 241))
        # create instance fot translate
        _translate = QtCore.QCoreApplication.translate
        
        # set widgets text
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do List "))
        self.add_item_pushButton.setText(_translate("MainWindow", "Add Task"))
        self.save_all_pushButton.setText(_translate("MainWindow", "Save Tasks"))
        self.delete_item_pushButton.setToolTip(_translate("MainWindow", "Delete Task"))
        self.clear_items_pushButton.setText(_translate("MainWindow", "Clear Tasks"))        
        # set text font
        self.lineEdit.setFont(QFont('times', 14))
        self.add_item_pushButton.setFont(QFont('times', 14 ))
        self.save_all_pushButton.setFont(QFont('Ariel', 14))
        self.delete_item_pushButton.setFont(QFont('times', 14))
        self.clear_items_pushButton.setFont(QFont('times', 14))
        self.listWidget.setFont(QFont('times', 14))
        # set tooltip text to display it while user hover over the widget
        self.lineEdit.setToolTip(_translate("MainWindow", "Enter Task"))
        self.add_item_pushButton.setToolTip(_translate("MainWindow", "Add Task"))
        self.save_all_pushButton.setToolTip(_translate("MainWindow", "Save all Tasks"))
        self.delete_item_pushButton.setText(_translate("MainWindow", "Delete Task"))
        self.clear_items_pushButton.setToolTip(_translate("MainWindow", "Clear Tasks"))
        # set place holder text for entry i.e lineEdit widget
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Task"))
        # call get_items() method to display
        # all tasks from database
        self.get_items()
    def get_items(self):
        # connect to database
        conn = sqlite3.connect('todo.db')
        # enable data manipulation
        cur = conn.cursor()
        # select data from table
        cur.execute('SELECT * FROM todo_list')
        # fetch data
        rows = cur.fetchall()
        # commit new changes 
        conn.commit()
        # close connection
        conn.close()
        # iterate through each row
        for row in rows:
            # add data in list 
            self.listWidget.addItem(str(row[0]))
    def add_item(self):
        
        # get user entered item
        item = self.lineEdit.text()
        # add entered item in list
        self.listWidget.addItem(item)
        # clear item entry        
        item = self.lineEdit.setText("")
    
    def save_all_items(self):
        # connect to database
        conn = sqlite3.connect('todo.db')
        # enable data manipulation
        cur = conn.cursor()
        # delete data from table
        cur.execute('DELETE FROM todo_list')
        # create empty list to
        # store items of list widget
        items = []
        # iterate throgh list widget items
        for i in range(self.listWidget.count()):
            # append each item to items list
            items.append(self.listWidget.item(i))
        # iterate through items list
        for item in items:
            # insert items into table
            cur.execute("INSERT INTO todo_list VALUES (:item)",{'item':item.text()})
        # commit new changes
        conn.commit()
        # close connection
        conn.close()       
    def delete_item(self):
        # get index number for selected row or item
        clicked = self.listWidget.currentRow()
        # delete item from list widget
        self.listWidget.takeItem(clicked)
    def clear_item(self):
        # clear list items
        self.listWidget.clear()
  
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = To_Do()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())