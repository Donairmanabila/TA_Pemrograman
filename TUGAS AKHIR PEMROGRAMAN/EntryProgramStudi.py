import sys
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

from CreateTableProgramStudi import MainForm

class MainForm(QDialog):
    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        # load file .ui yg dibuat di qt designer
        loadUi("C:\\Users\\Lenovo\\Documents\\TUGAS KULIAH SEMESTER 2\\PEMROGRAMAN\\TUGAS AKHIR PEMROGRAMAN\\EntryProgramStudi.ui",self)

        self.mode = -1 # 0: mode tambah, 1: mode ubah

        if self.mode == 0:
            self.txtNamaProdi.tableclear()
            self.txtNamaKaprodi.tableclear()

        self.btnOK.clicked.connect(self.accept)
        self.btnBatal.clicked.connect(self.reject)
        
if __name__ =="__main__":
    app = QApplication(sys.argv)
    w = MainForm()
    sys.exit(app.exec_())
    