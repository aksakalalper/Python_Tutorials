import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelBinarizer
from sklearn import neighbors
from sklearn.metrics import accuracy_score,mean_absolute_error,mean_squared_error,r2_score

# öğrenci boy ve kiloları girilir. cinsiyetleri girilir.
x_train=np.array([[160,65],[170,85],[185,85],[188,82],[155,50]])
y_train=['K','E','E','K','K']

# grafiğe dökülür.
plt.title('cinsiyet/boy')
plt.xlabel('boy')
plt.ylabel('kilo')
for i,x in enumerate(x_train):
    plt.scatter(x[0],x[1],c='k',marker='x'if y_train[i]=='E' else 'D')
plt.grid(True)
#plt.show()
# harf olarak girilen cinsiyetler nümerik hale getirilir.
lb=LabelBinarizer()
y_train=lb.fit_transform(y_train)
#knn modeli eğitilir
n_neighbors=3 #en yakın komşu sayısı 3 olsun
clf=neighbors.KNeighborsClassifier(n_neighbors,weights='distance')
clf.fit(x_train,y_train)
#model tahmin ettirilir.
print("tahmin edilen eğitim değerleri", clf.predict(x_train))
x_test=np.array([[170,65],[190,85],[145,85],[178,72]])
y_test=['K','E','K','E']
y_test=lb.transform(y_test)
print("ikili kategorik etiketler", y_test.T[0])
y_pred=clf.predict(x_test)
print("tahmin değerleri",y_pred)
print("etiketler",lb.inverse_transform(y_pred))
#sonuçlar yazdırılır
print('doğruluk oranı',accuracy_score(y_test,y_pred))
#hata matrisi oluşturma
from yellowbrick.classifier import ConfusionMatrix
kategori=['E','K']
cm=ConfusionMatrix(clf)
cm.fit(x_train,y_train)
print(cm.score(x_test,y_test))
cm.poof()
plt.show()
#model değerlendirmesini gösterme. bunlar regresyonda daha başarılıdır.
print("r2",r2_score(y_test,y_pred))
print("mae",mean_absolute_error(y_test,y_pred))
print("mse",mean_squared_error(y_test,y_pred))