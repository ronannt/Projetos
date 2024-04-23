import sys
import os
import PyQt5
import shutil
import ctypes
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from funcs import Funcs
from win32com.client import Dispatch

myDir = os.getcwd()
sys.path.append(myDir)
app = QtWidgets.QApplication([])

cod = "nada"

def get_version_via_com(filename):
    parser = Dispatch("Scripting.FileSystemObject")
    try:
        version = parser.GetFileVersion(filename)
    except Exception:
        return None
    return version

if __name__ == "__main__":

    paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
    version = list(filter(None, [get_version_via_com(p) for p in paths]))[0]
    verfor = int(version[2])

    pypath = sys.executable
    n = 10
    dest = pypath[:-n]
    dest2 = f"{myDir}\\ChromeDrivers\\"

    print(f"Caminho de destino: {dest}")

    if verfor == 9:
        print("Versão 109")
        scr = f"{myDir}\\ChromeDrivers\\109\\chromedriver.exe"
        shutil.copy(scr, dest2)
    elif verfor == 0:
        print("Versão Chrome 110")
        scr = f"{myDir}\\ChromeDrivers\\110\\chromedriver.exe"
        shutil.copy(scr, dest2)

    elif verfor == 1:
        print("Versão 111")
        scr = f"{myDir}\\ChromeDrivers\\111\\chromedriver.exe"
        shutil.copy(scr, dest2)
    else:
        print("Versão do Navegador Chrome divergente dos Drivers!")

    if not ctypes.windll.shell32.IsUserAnAdmin():
        print('Sem privilégios suficientes. Reiniciando...')
        ctypes.windll.shell32.ShellExecuteW(
            None, 'runas', sys.executable, ' '.join(sys.argv), None, None)
    else:
        print('Privilégios superiores garantidos')

    scr2 = f"{myDir}\\ChromeDrivers\\chromedriver.exe"
    try:
        shutil.move(scr2, dest)
        print("Pasta copiada.")
    except:
        print("Pasta ja existe.")

#Carregamento de telas
login = uic.loadUi("login.ui")

#Login
login.frame_erro.hide()
login.bt_cl_popup.clicked.connect(lambda: Funcs.ClosePopUp(login))

login.show()
app.exec_()