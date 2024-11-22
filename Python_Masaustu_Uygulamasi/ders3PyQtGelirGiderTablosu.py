import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow 
from income import Ui_MainWindow 

class Table(QMainWindow):
    def __init__(self):
        super(Table, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calcButton.clicked.connect(self.calculate)

    def calculate(self):
        sender = self.sender().text()
        result = 0
        if sender == "Hesapla":
            income = float(self.ui.totalIncome.text())
            total_taxes = float(self.ui.totalTaxes.text())
            total_fee = float(self.ui.totalFee.text())
            total_bank = float(self.ui.totalBank.text())
            outcome = total_taxes + total_fee + total_bank
            result = income - outcome
        self.ui.netIncome.setText(str(result))
        
def window():
    ## Atamalar yapilir
    app=QApplication(sys.argv) #sistem argümanı eklendi.
    win=Table() #pencere şeklindeki uygulamanın ataması yapıldı.
    win.show() #pencere gösterildi.
    sys.exit(app.exec_()) #exit tuşuna basınca uygulamadan çıkılır.

window()
