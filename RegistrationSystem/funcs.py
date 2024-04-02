import sys
import os
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
import time
import mysql.connector
from mysql.connector import errorcode
myDir = os.getcwd()
sys.path.append(myDir)


class Funcs:
    user = ""
    def ClosePopUp(window):
        window.frame_erro.hide()
    def ShowWindow(self, wind):
        wind.show()

    def Login(self, userget, paswget, login, wind):
        global user
        try:
            self.db_connection = mysql.connector.connect(host='localhost', user=userget, password=paswget, database='test')
            print("Banco de dados conectado!")
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
                login.close()
                Funcs.UpdateTable(Funcs, wind)
                wind.show()
                user = userget

    def UpdateTable(self, wind):
        self.cursor = self.db_connection.cursor()
        q = ("SELECT codigo, responsavel, status, obs FROM test.customers WHERE 1;")
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        table = wind.table
        table.setRowCount(len(result))
        table.setColumnCount(4)
        for i in range(0, len(result)):
            for j in range(0, 4):
                table.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))
        wind.show()
        self.cursor.close()

    '''def NewData(self, nome, rg, cpf,nascimento):
        setorf = setor.currentItem().text()

        if status1.isChecked():
            statusf = "Documentação"
        if status2.isChecked():
            statusf = "Análise"
        if status3.isChecked():
            statusf = "Vistoria"

        if obs == "":
            obs = "Nulo"
        obsf = ""
        for i in obs:
            if i.isalnum() or i == " ":
                    obsf += i
        obsf.lower()

        self.cursor = self.db_connection.cursor()
        self.cursor.execute(
            f"INSERT INTO test.base_projetos (setor, status, responsavel, obs) VALUES ('{setorf}', '{user}', '{statusf}', '{obsf}');")
        self.db_connection.commit()
        self.cursor.close()

        Funcs.UpdateTable(Funcs, wind)
        Funcs.ClearAdd(Funcs, setor, add, status1, status2, status3)
        add.close()'''