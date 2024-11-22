import pandas as pd
import numpy as np
from sklearn import tree
import matplotlib.pyplot as plt

# dosya okuma işlemleri yapılır
file="golf_oynama_veri_seti.xlsx"
data=pd.read_excel(file)
df=pd.DataFrame(data)
print(df.head(),"\n",df.info(),"\n",df.describe())

# x ve y eksen atamalari yapilir. veriler düzenlenir.
df['ruzgar'] = df['ruzgar'].map({'evet': 1, 'hayir':0}) # evet ve hayır cevapları 1-0 şeklinde yazdırıldı.
df=pd.get_dummies(data=df,columns=['hava','sicaklik','nem']) # diğer öğeler gruplandırıldı.
y=df["karar"] # bağımlı değişken seçildi.
yEncoded=y.map({'oyna': 1, 'oynama':0})
xEncoded=df.drop(['karar'],axis=1) # bağımsız değişkenler seçildi.
print("x",xEncoded)
print("y",yEncoded)
# veriler ağaç yapısına sokulur ve öğretilir.
decisionTree=tree.DecisionTreeClassifier(random_state=12345)
decisionTree=decisionTree.fit(xEncoded,yEncoded)
# ağaç yapısını metin şeklinde gösterir.
print(tree.export_text(decisionTree)) #ağaç yapısını metin şeklinde gösterir.
# ağaç yapısını matplotlib ile gösterir.
fig=tree.plot_tree(decisionTree,filled=True,rounded=True,class_names=["oyna","oynama"],feature_names=xEncoded.columns)
#plt.show()

# kullanıcıdan değişkenler alınır.
ruzgar = int(input("ruzgar (0 veya 1 girin): ")) 
hava_bulutlu = int(input("hava_bulutlu (0 veya 1 girin): ")) 
hava_gunesli = int(input("hava_gunesli (0 veya 1 girin): ")) 
hava_yagmurlu = int(input("hava_yagmurlu (0 veya 1 girin): ")) 
sicaklik_ilik = int(input("sicaklik_ilik (0 veya 1 girin): ")) 
sicaklik_sicak = int(input("sicaklik_sicak (0 veya 1 girin): ")) 
sicaklik_soguk = int(input("sicaklik_soguk (0 veya 1 girin): ")) 
nem_dusuk = int(input("nem_dusuk (0 veya 1 girin): ")) 
nem_orta = int(input("nem_orta (0 veya 1 girin): ")) 
nem_yuksek = int(input("nem_yuksek (0 veya 1 girin): "))
degerler=np.array([ruzgar, hava_bulutlu, hava_gunesli, hava_yagmurlu, sicaklik_ilik, sicaklik_sicak, sicaklik_soguk, nem_dusuk, nem_orta, nem_yuksek])
print(decisionTree.predict(X=[degerler]))