import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow , QMessageBox,QLineEdit, QInputDialog
from listview import  Ui_MainWindow

class Listview(QMainWindow):
    def __init__(self):
        super(Listview, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #buton atamalari yapilir.
        self.ui.btnExit.clicked.connect(self.exitApp)
        self.ui.btnSort.clicked.connect(self.sortStudent)
        self.ui.btnUp.clicked.connect(self.upStudent)
        self.ui.btnDown.clicked.connect(self.downStudent)
        self.ui.btnEdit.clicked.connect(self.editStudent)
        self.ui.btnAdd.clicked.connect(self.addStudent)
        self.ui.btnDelete.clicked.connect(self.deleteStudent)

        #ilk liste hazır olarak yüklendi.
        self.loadStudents()

    def loadStudents(self):
        self.ui.listItems.addItems(["Ahmet","Ali","Ada"])
    def addStudent(self):
        text,ok=QInputDialog.getText(self,"New student","Student Name")
        if text and ok is not None:
            self.ui.listItems.insertItem(0,text)
    def editStudent(self):
        index=self.ui.listItems.currentRow()
        item=self.ui.listItems.item(index)
        if item is not None:
            text,ok=QInputDialog.getText(self,"Edit Student","New Student name",QLineEdit.Normal,item.text())
            if text and ok is not None:
                item.setText(text)
    def deleteStudent(self):
        index=self.ui.listItems.currentRow()
        item=self.ui.listItems.item(index)
        if item is None:
            return
        q=QMessageBox.question(self,"Delete student","Are you sure to delete?",QMessageBox.Yes | QMessageBox.No)
        if q==QMessageBox.Yes:
            item=self.ui.listItems.takeItem(index)
            del item
    def upStudent(self):
        index=self.ui.listItems.currentRow()
        if index >=1:
            item=self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index-1,item)
            self.ui.listItems.setCurrentItem(item)
    def downStudent(self):
        index=self.ui.listItems.currentRow()
        if (index< (self.ui.listItems.count()-1)):
            item=self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index+1,item)
            self.ui.listItems.setCurrentItem(item)
    def sortStudent(self):
        self.ui.listItems.sortItems()
    def exitApp(self):
        QtWidgets.qApp.quit()

def window():
    ## Atamalar yapilir
    app=QApplication(sys.argv) #sistem argümanı eklendi.
    win=Listview() #pencere şeklindeki uygulamanın ataması yapıldı.
    win.show() #pencere gösterildi.
    sys.exit(app.exec_()) #exit tuşuna basınca uygulamadan çıkılır.

window()
