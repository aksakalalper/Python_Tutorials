import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow 
from combobox import Ui_MainWindow 

class Combobox(QMainWindow):
    def __init__(self):
        super(Combobox,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnGetItem.clicked.connect(self.getItems)  
        self.ui.btnLoadItem.clicked.connect(self.loadItems)  
        self.ui.btnDeleteItem.clicked.connect(self.deleteItem)

        self.ui.cbSehirler.currentIndexChanged.connect(self.selectedChanged)
        self.ui.cbSehirler.currentIndexChanged[str].connect(self.selectedChangedText)

        self.ui.cbSehirler.addItem("Kocaeli")
        self.ui.cbSehirler.addItem("İzmir")
        self.ui.cbSehirler.addItem("İstanbul")
        self.ui.cbSehirler.addItems(["Adana","Ankara"])

    #itemler yüklenir.
    def loadItems(self):
        sehirler=["Denizli","Afyon"]
        self.ui.cbSehirler.addItems(sehirler)

    #itemler eklenir.
    def getItems(self):
        print(self.ui.cbSehirler.currentText(),self.ui.cbSehirler.currentIndex())

    #index numarası değişince index bilgisi otomatik gelir.
    def selectedChanged(self,index):
        self.index=index

    def selectedChangedText(self,text):
        self.text=text
        print(self.index,self.text)
    #öğeler silinir
    def deleteItem(self):
        self.ui.cbSehirler.clear()

def app():
    ## Atamalar yapilir
    app=QApplication(sys.argv) #sistem argümanı eklendi.
    win=Combobox() #pencere şeklindeki uygulamanın ataması yapıldı.
    win.show() #pencere gösterildi.
    sys.exit(app.exec_()) #exit tuşuna basınca uygulamadan çıkılır.

app()

