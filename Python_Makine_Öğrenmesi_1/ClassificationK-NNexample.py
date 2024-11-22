import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn import neighbors
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

file="T-shirt.xlsx"
data=pd.read_excel(file)
df=pd.DataFrame(data)
print(df.info(),df.describe(),df.columns)
print(df.head())
le=LabelEncoder()
df['Beden']=le.fit_transform(df['Beden'])
print(le.classes_)
sns.countplot(data=df['Beden'])

x=df[['Boy','Kilo']]
y=df['Beden']

x_train, x_test, y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
accuracy_skorları=[]
for k in range(10):
    k=k+1
    knn=neighbors.KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    pred=knn.predict(x_test)
    accuracy=accuracy_score(y_test,pred)
    accuracy_skorları.append(accuracy)
    print(f"{k} için accuracy skoru {accuracy}")

from sklearn.neighbors import KNeighborsClassifier
n_neighbors=2
knn=KNeighborsClassifier(n_neighbors).fit(x_train,y_train)
knn.predict(x_train)
y_pred=knn.predict(x_test)

print("doğruluk oranı",accuracy_score(y_test,y_pred))

from yellowbrick.classifier import ConfusionMatrix
kategori=['S','M','L']
cm=ConfusionMatrix(knn)
cm=ConfusionMatrix(knn,classes=kategori,label_encoder={2:'S',1:'M',0:'S'})
cm.fit(x_train,y_train)
cm.score(x_test,y_test)
cm.poof()
plt.show()
