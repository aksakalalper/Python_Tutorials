import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow 
from heart_attack import Ui_MainWindow 


# dosya okuma işlemleri yapılır
file="heart.csv"
data=pd.read_csv(file)
df=pd.DataFrame(data)
print(df.head(),"\n",df.info(),"\n",df.describe())
df.drop_duplicates()
df=df.drop(['oldpeak', 'slp', 'caa', 'thall'],axis=1)
y=df['output']
x=df.drop(['output'],axis=1)
print(df.head())

# Eğitim ve test setlerine bölünür
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Karar ağacı modelini oluşturulur
clf = DecisionTreeClassifier()

# Model eğitim seti üzerinde eğitilir
clf.fit(X_train, y_train)

# Test seti üzerinde tahmin yapılır
y_pred = clf.predict(X_test)

# Modelin doğruluğuna bakılır
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Doğruluğu: {accuracy}")



class Checkbox(QMainWindow):
    def __init__(self):
        super(Checkbox,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

    def predict(self):
        
    # Kullanıcıdan veri alma
        user_data = {
    'age': int(input("Yaş: ")),
    'sex': int(input("Cinsiyet (Erkek: 1, Kadın: 0): ")),
    'cp': int(input("Göğüs Ağrısı Tipi (0-3): ")),
    'trtbps': int(input("Dinlenme Kan Basıncı: ")),
    'chol': int(input("Serum Kolestrol: ")),
    'fbs': int(input("Açlık Kan Şekeri > 120 mg/dl (Evet: 1, Hayır: 0): ")),
    'restecg': int(input("Dinlenme Elektrokardiyografi Sonuçları (0-2): ")),
    'thalachh': int(input("Maksimum Kalp Hızı: ")),
    'exng': int(input("Egzersizle İndüklenen Angina (Evet: 1, Hayır: 0): "))
        }

    # Kullanıcı verisini DataFrame'e çevir
        user_df = pd.DataFrame([user_data])

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # Model kullanarak tahmin yap
        user_prediction = clf.predict(user_df)

        if user_prediction[0] == 1:
         print("Tahmin: Kalp hastalığı mevcut.")
        else:
           print("Tahmin: Kalp hastalığı mevcut değil.")


def app():
    ## Atamalar yapilir
    app=QApplication(sys.argv) #sistem argümanı eklendi.
    win=Checkbox() #pencere şeklindeki uygulamanın ataması yapıldı.
    win.show() #pencere gösterildi.
    sys.exit(app.exec_()) #exit tuşuna basınca uygulamadan çıkılır.

app()
