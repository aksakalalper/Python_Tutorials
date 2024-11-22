import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow 
from radiobutton import Ui_MainWindow 

class Checkbox(QMainWindow):
    def __init__(self):
        super(Checkbox,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioButton.toggled.connect(self.onClickedUlke)
        self.ui.radioButton_2.toggled.connect(self.onClickedUlke)
        self.ui.radioButton_3.toggled.connect(self.onClickedUlke)
        self.ui.radioButton_4.toggled.connect(self.onClickedUlke)
        self.ui.radioButton_5.toggled.connect(self.onClickedEgitim)
        self.ui.radioButton_6.toggled.connect(self.onClickedEgitim)
        self.ui.radioButton_7.toggled.connect(self.onClickedEgitim)
        self.ui.radioButton_8.toggled.connect(self.onClickedEgitim)

    def onClickedUlke(self):
        rb=self.sender()
        if rb.isChecked():
            self.ui.labelUlke.setText(f"secilen kutucuk {rb.text()}")
            self.res1=str(f"secilen kutucuk {rb.text()}")
    def onClickedEgitim(self):
        rb=self.sender()
        if rb.isChecked():
            self.ui.labelEgitim.setText(f"secilen kutucuk {rb.text()}")


def app():
    ## Atamalar yapilir
    app=QApplication(sys.argv) #sistem argümanı eklendi.
    win=Checkbox() #pencere şeklindeki uygulamanın ataması yapıldı.
    win.show() #pencere gösterildi.
    sys.exit(app.exec_()) #exit tuşuna basınca uygulamadan çıkılır.

app()

