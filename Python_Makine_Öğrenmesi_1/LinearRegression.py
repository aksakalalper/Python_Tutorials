import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

# veri bilgileri alınır.
data={
    'km':[6000,8200,9000,14200,16200],
    'fiyat':[86000,82000,78000,75000,70000]
}
#dataframe oluşturulur.
df=pd.DataFrame(data=data)
x=df['km']
y=df['fiyat']
#grafik oluşturulur.
xModel = np.array([x]).reshape(-1, 1) 
model = LinearRegression() 
result = model.fit(xModel,y)
yPredictions=model.predict(xModel)

def graphic():
    plt.plot(x,y,marker='o')
    plt.xlabel('araç km')
    plt.ylabel('fiyat')
    plt.legend()
    plt.show()
#lineer regresyona sokulur. model parametre katsayıları alınır.(y= α+β.x)
def LinearRegressionModel():
    print("kesim parametresi: ",result.coef_[0])
    print("öznitelik katsayısı: " ,result.intercept_)
    #modelin tahmin doğrusu oluşturulur.
    plt.figure()
    plt.plot(x,y,marker='o')
    plt.plot(xModel,model.predict(xModel))
    plt.xlabel('araç km')
    plt.ylabel('fiyat')
    plt.legend()
    plt.grid(True)
    plt.show()
# fiyat tahmini yapıldı.
def predictPrice():
    km = np.array([[12000]]) 
    tahmin_fiyat = model.predict(km) 
    print(tahmin_fiyat[0])
def errors():
    print("MAE: ",mean_absolute_error(y,yPredictions))
    print("MSE: ",mean_squared_error(y,yPredictions))
    print("R2: ",r2_score(y,yPredictions))

# buraya kadar herşey tamam. eldeki veriler ile %92 doğrulukta başarı elde ettik. 
# peki bunların dışına çıkınca ne olacak.

def testTrain():
    xTest=np.array([[1700],[2600],[11000],[14000],[17500]]).reshape(-1,1)
    yTest=[94000,94400,73000,83000,75000]
    yTestPredictions=model.predict(xTest)
    plt.figure()
    plt.axis([0,20000,60000,95000])
    plt.plot(x,y,label='gerçek değer',marker='o')
    plt.plot(xModel,model.predict(xModel),label='tahmin edilen',marker='x')
    plt.plot(xTest,yTest,label='test verisi',marker='v')
    plt.plot(xTest,yTestPredictions,label='test sonucu')
    plt.legend()
    print("MAE: ",mean_absolute_error(yTest,yTestPredictions))
    print("MSE: ",mean_squared_error(yTest,yTestPredictions))
    print("R2: ",r2_score(yTest,yTestPredictions))  
    result2 = model.fit(xTest,yTest)
    print("kesim parametresi: ",result2.coef_[0])
    print("öznitelik katsayısı: " ,result2.intercept_)  
    plt.show()

testTrain()
