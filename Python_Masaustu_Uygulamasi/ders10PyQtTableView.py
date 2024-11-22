import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow , QTableWidgetItem, QMessageBox,QLineEdit, QInputDialog
from tableview import  Ui_MainWindow

class Tableview(QMainWindow):
    def __init__(self):
        super(Tableview, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadProducts()
        self.ui.btnSave.clicked.connect(self.saveProduct)
        self.ui.tableProducts.setHorizontalHeaderLabels(("name","price"))

    def loadProducts(self):
        products=[
            {'name':'samsung s5','price':'2000'},
            {'name':'samsung s6','price':'3000'},
            {'name':'samsung s7','price':'500'}
        ]
        self.ui.tableProducts.setRowCount(len(products))
        self.ui.tableProducts.setColumnCount(2)
        rowIndex=0
        for product in products:
            self.ui.tableProducts.setItem(rowIndex,0,QTableWidgetItem(product['name']))
            self.ui.tableProducts.setItem(rowIndex,1,QTableWidgetItem(str(product['price'])))
            rowIndex +=1
    def saveProduct(self):

        name=self.ui.inputName.text()
        price=self.ui.inputPrice.text()
        rowIndex=self.ui.tableProducts.rowCount()
        if name and price is not None:
            self.ui.tableProducts.insertRow(rowIndex)
            self.ui.tableProducts.setItem(rowIndex,0,QTableWidgetItem(name))
            self.ui.tableProducts.setItem(rowIndex,1,QTableWidgetItem(str(price)))

        


def window():
    ## Atamalar yapilir
    app=QApplication(sys.argv) #sistem argümanı eklendi.
    win=Tableview() #pencere şeklindeki uygulamanın ataması yapıldı.
    win.show() #pencere gösterildi.
    sys.exit(app.exec_()) #exit tuşuna basınca uygulamadan çıkılır.

window()
