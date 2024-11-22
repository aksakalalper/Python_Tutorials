import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow , QMessageBox
from datetimee import  Ui_MainWindow
from PyQt5.QtCore import QDate

class Datetime(QMainWindow):
    def __init__(self):
        super(Datetime, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnCalc.clicked.connect(self.calculate)

    def calculate(self):
        start=self.ui.dateStart.date()
        end=self.ui.dateEnd.date()
        startdate=start.toString("dd MMMM yyyy")
        enddate=end.toString("dd MMMM yyyy")
        print(startdate,"***",enddate)
        daysDifference=start.daysTo(end)
        print(daysDifference)

def window():
    ## Atamalar yapilir
    app=QApplication(sys.argv) #sistem argümanı eklendi.
    win=Datetime() #pencere şeklindeki uygulamanın ataması yapıldı.
    win.show() #pencere gösterildi.
    sys.exit(app.exec_()) #exit tuşuna basınca uygulamadan çıkılır.

window()
