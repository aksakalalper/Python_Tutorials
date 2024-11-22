import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow , QMessageBox
from messagebox import Ui_MainWindow 

class Messagebox(QMainWindow):
    def __init__(self):
        super(Messagebox, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnExit.clicked.connect(self.showDialog)
    
    #mesaj kutusu ile uygulamadan çıkıldı.
    def showDialog(self):
        result=QMessageBox.question(self,"are you sure?","are you sure?",QMessageBox.Ok | QMessageBox.Ignore | QMessageBox.Cancel)

        if result==QMessageBox.Ok:
            print("Yes clicked")
            QtWidgets.qApp.quit()
        else:
            print("No click")        

def window():
    ## Atamalar yapilir
    app=QApplication(sys.argv) #sistem argümanı eklendi.
    win=Messagebox() #pencere şeklindeki uygulamanın ataması yapıldı.
    win.show() #pencere gösterildi.
    sys.exit(app.exec_()) #exit tuşuna basınca uygulamadan çıkılır.

window()
