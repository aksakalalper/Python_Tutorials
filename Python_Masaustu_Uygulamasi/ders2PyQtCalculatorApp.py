import sys #komut satırından uygulama açmak için import edildi.
from PyQt5.QtWidgets import QApplication,QMainWindow
from calculator import Ui_MainWindow

class App(QMainWindow):
    def __init__(self):
        super(App,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.buttonAdd.clicked.connect(self.calc)
        self.ui.buttonSub.clicked.connect(self.calc)
        self.ui.buttonMul.clicked.connect(self.calc)
        self.ui.buttonDiv.clicked.connect(self.calc)
        

    def calc(self):
        sender=self.sender().text()
        result=0

        if (sender=="Toplama"):
            result=float(self.ui.textSayi1.text())+float(self.ui.textSayi2.text())
        if (sender=="Çıkarma"):
            result=float(self.ui.textSayi1.text())-float(self.ui.textSayi2.text())
        if (sender=="Çarpma"):
            result=float(self.ui.textSayi1.text())*float(self.ui.textSayi2.text())
        if (sender=="Bölme"):
            result=float(self.ui.textSayi1.text())/float(self.ui.textSayi2.text())
        
        self.ui.textSonuc.setText(str(result))       


def window():
    ## Atamalar yapilir
    app=QApplication(sys.argv) #sistem argümanı eklendi.
    win=App() #pencere şeklindeki uygulamanın ataması yapıldı.
    win.show() #pencere gösterildi.
    sys.exit(app.exec_()) #exit tuşuna basınca uygulamadan çıkılır.

window()