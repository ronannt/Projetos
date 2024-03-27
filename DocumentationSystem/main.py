import sys
import os
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from funcs import Funcs


myDir = os.getcwd()
sys.path.append(myDir)
app = QtWidgets.QApplication([])


'''Ícone usado nas janelas: href="https://www.flaticon.com/free-icons/digital-product" title="digital-product icons"Digital-product icons created by Freepik - Flaticon'''

#Carregamento de telas
login = uic.loadUi("Projetos\Frames\login.ui")
home = uic.loadUi("Projetos\Frames\home.ui")


#Login
login.frame_erro.hide()
login.bt_cl_popup.clicked.connect(lambda: Funcs.ClosePopUp(login))
login.bt_enter_login.clicked.connect(lambda: Funcs.Login(Funcs, login.line_user.text(), login.line_pass.text(), login, home))

#Home
home.frame_erro.hide()
home.bt_cl_popup.clicked.connect(lambda: Funcs.ClosePopUp(home))
home.bt_add.clicked.connect(lambda: Funcs.ShowWindow(Funcs, add))
home.bt_info.clicked.connect(lambda: Funcs.Select(Funcs, home.table, info, home))

login.show()
app.exec_()