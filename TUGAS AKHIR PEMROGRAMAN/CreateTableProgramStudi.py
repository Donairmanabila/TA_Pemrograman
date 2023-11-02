import sys
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi

tableDefinition=""

class MainForm(QDialog):
    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        loadUi("C:\\Users\\Lenovo\\Documents\\TUGAS KULIAH SEMESTER 2\\PEMROGRAMAN\\TUGAS AKHIR PEMROGRAMAN\\CreateTableProgramStudi.ui", self)
        self.ButtonAddColumn.clicked.connect(self.AddColumn)
        self.ButtonCreateTable.clicked.connect(self.CreateTable)

    def AddColumn(self):
        global tableDefinition
        if tableDefinition=="":
            tableDefinition="CREATE TABLE IF NOT EXISTS " + self.lineEditTableName.text() +" (" + self.lineEditColumnName.text()+" " + self.ComboBoxDataType.itemText(self.ComboBoxDataType.currentIndex())
            self.lineEditColumnName.setText("")
            self.lineEditColumnName.setFocus()
        else:
            tableDefinition+=","+self.lineEditColumnName.text()+ " " + self.ComboBoxDataType.itemText(self.ComboBoxDataType.currentIndex())
            self.lineEditColumnName.setText("")
            self.lineEditColumnName.setFocus()
    
    def CreateTable(self):
        global tableDefinition
        db = QSqlDatabase.addDatabase('QSQLITE')
        dbName = self.lineEditDBName.text()+".db"
        db.setDatabaseName(dbName)
        tableName = self.lineEditTableName.text()
        if db.open():
            tableDefinition+=");"
            query = QSqlQuery()
            query.exec_(tableDefinition)
            self.labelResponse.setText("Table %s is successfully created" %tableName)
        else:
            self.labelResponse.setText("Error in creating table")

if __name__ =="__main__":
    app = QApplication(sys.argv)
    w = MainForm()
    w.show()
    sys.exit(app.exec_())