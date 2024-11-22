import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow 
from checkbox import Ui_MainWindow 

class App(QMainWindow):
    def __init__(self):
        super(App,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cbSinema.stateChanged.connect(self.showState)
        self.ui.cbSpor.stateChanged.connect(self.showState)
        self.ui.cbGezi.stateChanged.connect(self.showState)

        self.ui.btnKayit.clicked.connect(self.getAllChecked)
        self.ui.btnKayit_2.clicked.connect(self.getResults)

    def showState(self,value):
        cb=self.sender()
        print(cb.text(),cb.isChecked())
        
        
    def getAllChecked(self):
        result=""
        items=self.ui.groupBox.findChildren(QtWidgets.QCheckBox)
        print(items)
        for cb in items:
            if cb.isChecked():
                print(cb.text())
                print(cb.isChecked())
                result += cb.text()+"\n"
            
        self.ui.lblResult.setText(result)
        
    
    def getResults(self):
        result=""
        items=self.ui.groupBox_2.findChildren(QtWidgets.QCheckBox)
        print(items)
        for cb in items:
            if cb.isChecked():
                print(cb.text())
                print(cb.isChecked())
                result += cb.text()+"\n"

        self.ui.lblResult_2.setText(result)


def app():
    ## Atamalar yapilir
    app=QApplication(sys.argv) #sistem argümanı eklendi.
    win=App() #pencere şeklindeki uygulamanın ataması yapıldı.
    win.show() #pencere gösterildi.
    sys.exit(app.exec_()) #exit tuşuna basınca uygulamadan çıkılır.

app()

    