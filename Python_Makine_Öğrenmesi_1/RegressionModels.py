import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split,GridSearchCV,cross_val_score
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error
from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet,SGDRegressor
from sklearn.preprocessing import PolynomialFeatures,MinMaxScaler
from sklearn.pipeline import make_pipeline

file="Audi_A1_listings.csv"
data=pd.read_csv(file)
df=pd.DataFrame(data)
y=df['Price(£)']
df=df.drop(columns=['index','href','MileageRank','PriceRank','PPYRank','Score','Type'])
df['Engine']=df['Engine'].str.replace('L',' ')
df['Engine'] = pd.to_numeric(df['Engine'], errors='coerce')
df=pd.get_dummies(df,columns=['Transmission','Fuel'],drop_first=True)
x=df.drop('Price(£)',axis=1)
print(df.info(),df.describe(),df.columns)
xTrain,xTest,yTrain,yTest=train_test_split(x,y,test_size=0.3,random_state=22)
print(xTrain.shape)
print(yTrain.shape)
print(df.head(5))
model=LinearRegression()
def graphics():
    plt.figure()
    corr=df.corr()
    sns.heatmap(data=corr,annot=True)
    sns.displot(df['Fiyat'])
    plt.show()
def linearRegression():
    model.fit(xTrain,yTrain)
    yTrainPred=model.predict(xTrain)
    yTestPred=model.predict(xTest)
    print("eğitim verisi için r2:",r2_score(yTrain,yTrainPred))
    print("test verisi için r2: ",r2_score(yTest,yTestPred))

def lassoRegression():
    lasso=Lasso()
    lasso.fit(xTrain,yTrain)
    trainScore=lasso.score(xTrain,yTrain)
    testScore=lasso.score(xTest,yTest)
    coeff_used=np.sum(lasso.coef_!=0)
    print("eğitim verisi için r2:", trainScore)
    print("test verisi için r2: ",testScore)
    print("sıfırdan büyük öznitelikler: ",coeff_used)
    lasso001=Lasso(alpha=0.01)
    lasso001.fit(xTrain,yTrain)
    trainScore=lasso001.score(xTrain,yTrain)
    testScore=lasso001.score(xTest,yTest)
    coeff_used=np.sum(lasso001.coef_!=0)
    print("eğitim verisi için r2:", trainScore)
    print("test verisi için r2: ",testScore)
    print("sıfırdan büyük öznitelikler: ",coeff_used)
    lasso0001=Lasso(alpha=0.001)
    lasso0001.fit(xTrain,yTrain)
    trainScore=lasso0001.score(xTrain,yTrain)
    testScore=lasso0001.score(xTest,yTest)
    coeff_used=np.sum(lasso0001.coef_!=0)
    print("eğitim verisi için r2:", trainScore)
    print("test verisi için r2: ",testScore)
    print("sıfırdan büyük öznitelikler: ",coeff_used)

def ridgeRegression():
    ridge001=Ridge(alpha=0.01)
    ridge001.fit(xTrain,yTrain)
    trainScore=ridge001.score(xTrain,yTrain)
    testScore=ridge001.score(xTest,yTest)
    coeff_used=np.sum(ridge001.coef_!=0)
    print("eğitim verisi için r2:", trainScore)
    print("test verisi için r2: ",testScore)
    print("sıfırdan büyük öznitelikler: ",coeff_used)
    ridge0001=Ridge(alpha=0.001)
    ridge0001.fit(xTrain,yTrain)
    trainScore=ridge0001.score(xTrain,yTrain)
    testScore=ridge0001.score(xTest,yTest)
    coeff_used=np.sum(ridge0001.coef_!=0)
    print("eğitim verisi için r2:", trainScore)
    print("test verisi için r2: ",testScore)
    print("sıfırdan büyük öznitelikler: ",coeff_used)

def elasticNet():
    enet=ElasticNet()
    enet.fit(xTrain,yTrain)
    trainScore=enet.score(xTrain,yTrain)
    testScore=enet.score(xTest,yTest)
    coefUsed=np.sum(enet.coef_!=0)
    print("trainScore: ",trainScore)
    print("testScore: ",testScore)
    print("coefUsed: ",coefUsed)
    enet001=ElasticNet(alpha=0.01)
    enet001.fit(xTrain,yTrain)
    trainScore=enet001.score(xTrain,yTrain)
    testScore=enet001.score(xTest,yTest)
    coefUsed=np.sum(enet001.coef_!=0)
    print("trainScore: ",trainScore)
    print("testScore: ",testScore)
    print("coefUsed: ",coefUsed)
    enet100=ElasticNet(alpha=100)
    enet100.fit(xTrain,yTrain)
    trainScore=enet100.score(xTrain,yTrain)
    testScore=enet100.score(xTest,yTest)
    coefUsed=np.sum(enet100.coef_!=0)
    print("trainScore: ",trainScore)
    print("testScore: ",testScore)
    print("coefUsed: ",coefUsed)

def gridSearchLasso():
    lasso=Lasso(random_state=42)
    parametreler={'alpha':[0.000000000000001,0.00000000001,0.000000001,0.0000001,0.00001,0.001,1,2,3,4,5,10,20,30,50]}
    #grid search fonksiyonundaen iyi sonucu almak için scoring(r2):2 girilir.
    #cv parametresi kaç defa rassal olarak veri setini böleceğini belirler.
    lasso_GS=GridSearchCV(lasso,parametreler,scoring='r2',cv=5)
    lasso_GS.fit(xTrain,yTrain)
    print(lasso_GS.best_params_)
    print(lasso_GS.best_estimator_)

def gridSearchEnet():
    enet=ElasticNet(random_state=42)
    parametreler={'alpha':[0.000000000000001,0.00000000001,0.000000001,0.0000001,0.00001,0.001,1,2,3,4,5,10,20,30,50],
                  'l1_ratio':[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]}
    enet_GS=GridSearchCV(enet,parametreler,scoring='r2',cv=5)
    enet_GS.fit(xTrain,yTrain)
    print(enet_GS.best_params_)
    print(enet_GS.best_estimator_)
    enetTrainScore=enet_GS.best_estimator_.score(xTrain,yTrain)
    enetTestScore=enet_GS.best_estimator_.score(xTest,yTest)
    print(enetTrainScore)
    print(enetTestScore)
    data['Fiyat Tahmini']=enet_GS.best_estimator_.predict(x)
    print(data[['Fiyat','Fiyat Tahmini']].head(20))
    plt.scatter(data['Fiyat'],data.index.values,label='gerçek fiyat')
    plt.scatter(data["Fiyat Tahmini"],data.index.values,label='tahmini fiyat')
    plt.legend()
    plt.show()

def polynominalRegression():
    #graph=sns.pairplot(df)
    graph=sns.pairplot(df,y_vars=['Fiyat'],x_vars=['Oda_Sayısı','Net_m2','Katı','Yaşı'],height=4)
    graph.map(sns.regplot,color='red')
    plt.show()

def stokastikGradientDescent():
    xScaler=MinMaxScaler()
    yScaler=MinMaxScaler()
    X=xScaler.fit_transform(x)
    Y=yScaler.fit_transform(y.values.reshape(-1,1))
    sgd_reg=SGDRegressor(random_state=42,penalty='elasticnet')
    parametreler={'alpha':[0.0001,0.001,0.01,0.1],
                    'eta0':[0.0001,0.001,0.01,0.1],
                    'l1_ratio':[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],
                    'learning_rate':['constant','optimal','invscaling','adaptive'],
                    'max_iter':[50,100,500,1000]}
    sgd_reg_GS=GridSearchCV(estimator=sgd_reg,param_grid=parametreler,n_jobs=-1,scoring='r2',cv=5)
    sgd_reg_GS.fit(xTrain,yTrain)
    print(sgd_reg_GS.best_params_)
    print(sgd_reg_GS.best_estimator_)
    print(sgd_reg_GS.best_score_)
ridgeRegression()
