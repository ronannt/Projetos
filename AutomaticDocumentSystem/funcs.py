from __future__ import annotations
import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
import docx
from docx import Document
from openpyxl import *
from datetime import date
import shutil
from docx.shared import Inches
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
import time
import pyautogui
from selenium import webdriver
from win32com.client import Dispatch
import mysql.connector
from mysql.connector import errorcode
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem


class Funcs:
    def ClosePopUp(window):
        window.frame_erro.hide()

    def Login(self, userget, paswget, login, home):
        try:
            self.db_connection = mysql.connector.connect(host='localhost', user=userget, password=paswget, database='ntc_clientes')
            print("Banco de dados conectado!")
            self.cursor = self.db_connection.cursor()
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                login.label_erro.setText("Servidor não disponivel!")
                login.frame_erro.show()
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                login.label_erro.setText("Usuário e senha inválido!")
                login.frame_erro.show()
            else:
                login.label_erro.setText("Erro desconhecido!")
                login.frame_erro.show()
                print(error)
        else:
                print("Conectado!")
                #home.show()
                login.close()
                home.show()

    def ShowWindow(wind):
        wind.show()