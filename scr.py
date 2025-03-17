from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget , QPushButton , QLabel , QVBoxLayout , QHBoxLayout, QRadioButton
from time import sleep
from random import  randint
app=QApplication([])
main_win=QWidget()

main_win.setWindowTitle("Конкурс")
main_win.move(100,200)

radio1=QRadioButton("2010")
radio2=QRadioButton("2011")
radio3=QRadioButton("2012")
radio4=QRadioButton("2013")
label= QLabel("У якому році вийшов Скайрім?")

vertical=QVBoxLayout()
notvertical1=QHBoxLayout()
notvertical2=QHBoxLayout()
notvertical3=QHBoxLayout()

notvertical1.addWidget(label,alignment=Qt.AlignCenter)

notvertical2.addWidget(radio1,alignment=Qt.AlignCenter)
notvertical2.addWidget(radio2,alignment=Qt.AlignCenter)

notvertical3.addWidget(radio3,alignment=Qt.AlignCenter)
notvertical3.addWidget(radio4,alignment=Qt.AlignCenter)

vertical.addLayout(notvertical1)
vertical.addLayout(notvertical2)
vertical.addLayout(notvertical3)

main_win.setLayout(vertical)
def show_win():
     win=QMessageBox()
     win.setText("Вірно.")
     win.show()
     win.exec_()
     main_win.hide()

def show_nowin():
     nowin=QMessageBox()
     nowin.setText("Ні, у 2011 році.")
     nowin.show()
     nowin.exec_()
     main_win.hide()
radio1.clicked.connect(show_nowin)
radio2.clicked.connect(show_win)
radio3.clicked.connect(show_nowin)
radio4.clicked.connect(show_nowin)

main_win.show()

app.exec_()