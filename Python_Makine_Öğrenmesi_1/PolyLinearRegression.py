import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

file="SATILIK_EV1.xlsx"
data=pd.read_excel(file)
df=pd.DataFrame(data=data)
df=df.drop(['Unnamed: 0'],axis=1)
print(df.columns)
x=df[['Oda_Sayısı', 'Net_m2','Katı', 'Yaşı']]
y=df['Fiyat']
model=LinearRegression()

def graphics():
    plt.figure()
    corr=df.corr()
    sns.heatmap(data=corr,annot=True)
    sns.displot(df['Fiyat'])
    plt.show()

def testTrain():
    xTrain,xTest,yTrain,yTest=train_test_split(x,y,test_size=0.2,random_state=42)
    result=model.fit(xTrain,yTrain)
    print("öznitelik katsayısı: ",result.intercept_)
    print("kesme parametresleri: ",result.coef_)

def predict():
    xTrain,xTest,yTrain,yTest=train_test_split(x,y,test_size=0.2,random_state=42)
    model.fit(xTrain,yTrain)
    yTrainTest=model.predict(xTrain)
    print(r2_score(yTrain,yTrainTest))
    yTestTest=model.predict(xTest)
    print(r2_score(yTest,yTestTest))
    plt.scatter(yTrain,yTrainTest)
    plt.show()

testTrain()

print(model.predict([[3,105,4,8]]))