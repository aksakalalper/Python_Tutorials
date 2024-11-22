from sklearn.linear_model import LinearRegression,Lasso,Ridge,ElasticNet,LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error,mean_absolute_percentage_error,r2_score
from sklearn.tree import DecisionTreeClassifier,export_graphviz
from sklearn import tree
from sklearn.preprocessing import MinMaxScaler,StandardScaler,LabelEncoder
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor   
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import graphviz
import xgboost as xgb


#class created
class LinearRegressionModels():
    def __init__(self):
        self.lm=LinearRegression()
    #simple linear regression model
    def linearRegression(self):
        #reading files
        file="Student_Marks.csv"
        data=pd.read_csv(file)
        df=pd.DataFrame(data)
        y=df['Marks'] #we want to predict that 
        x=df.drop('Marks',axis=1)
        model=self.lm.fit(x,y) #learning process
        print("modelin skoru: ",model.score(x,y))
        print("modelin coef sabiti: ",model.coef_)
        print("modelin intercept katsayısı: ",model.intercept_)
        print("tahmin edilen değer: ",model.predict([[5,4]]))
    #preparing data for learning process
    def preProcessingTrainTestSplit(self):
        #reading files
        file="Audi_A1_listings.csv"
        data=pd.read_csv(file)
        df=pd.DataFrame(data)
        df=df.drop(['index', 'Type' ,'Number_of_Owners', 'href', 'MileageRank', 'PriceRank', 'PPYRank', 'Score'],axis=1)
        df['Engine']=df['Engine'].str.replace('L',' ')
        df['Engine']=pd.to_numeric(df['Engine'])
        df=pd.get_dummies(df,columns=['Transmission','Fuel'])
        y=df['Price(£)']
        x=df.drop('Price(£)',axis=1)
        model=self.lm.fit(x,y)
        print(df.info(),"\n",df.describe(),"\n",df.columns)
        print(df.head(5))
        print("model skoru", model.score(x,y))
        #train-test-split
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
        trainModel=self.lm.fit(x_train,y_train)
        print("train model skoru: ", trainModel.score(x_test,y_test))
    def mseRMSEmae(self):
        #reading files
        file="insurance.csv"
        data=pd.read_csv(file)
        df=pd.DataFrame(data)
        df=pd.get_dummies(df,columns=['sex','smoker','region'])
        y=df['charges']
        x=df.drop('charges',axis=1)
        model=self.lm.fit(x,y)
        y_pred=model.predict(x)
        print(model.score(x,y))
        print("model mae: ",mean_absolute_error(y,y_pred))
        print("model mse: ",mean_squared_error(y,y_pred))
        print("model mape: ",mean_absolute_percentage_error(y,y_pred))
        print("model r2 score: ",r2_score(y,y_pred)) #model performance
    def fittingTypes(self):
        #overfittting: learning more than estimated. it's like memorising. model can predict the future.
        #underfitting: learning less than estimated. model can't predict the future.
        #balancedfitting: learning balanced
        #this dataset comes with seaborn library.
        df=sns.load_dataset('diamonds')
        df=pd.get_dummies(df,columns=['cut','color','clarity'])
        y=df['price']
        x=df.drop('price',axis=1)
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
        lm=self.lm
        model=lm.fit(x_train,y_train)
        print('train score: ',model.score(x_train,y_train))
        print('test score: ',model.score(x_test,y_test))
    def ridgeRegression(self):
    #it's being used for overfitting situation.
    #it fixes bias and variance.
    #it fixes features. it makes features coefficent near to zero but not zero!
        #reading files
        file="Student_Marks.csv"
        data=pd.read_csv(file)
        df=pd.DataFrame(data)
        y=df['Marks'] #we want to predict that 
        x=df[['time_study']]
        plt.style.use('fivethirtyeight')
        plt.scatter(x,y)
        #plt.show()
        model=self.lm.fit(x,y)
        print("model score:",model.score(x,y))
        alfa=[0.5,1,5,10,100]
        for index in alfa:
            modelr=Ridge(alpha=index )
            result=modelr.fit(x,y)
            print('score after ridge regression: ',result.score(x,y))
    def logisticRegression(self):
        file="UCI_Credit_Card.csv"
        data=pd.read_csv(file)
        df=pd.DataFrame(data)
        df=df.drop('ID',axis=1)
        y=df['default.payment.next.month']
        x=df.drop('default.payment.next.month',axis=1)
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
        lr=LogisticRegression()
        model=lr.fit(x_train,y_train)
        print("train score: ",model.score(x_train,y_train))
        print("test score: ",model.score(x_test,y_test))
    def decisionTree(self):
        file="heart.csv"
        data=pd.read_csv(file)
        df=pd.DataFrame(data)
        y=df['output']
        x=df.drop('output',axis=1)
        trees=DecisionTreeClassifier()
        model=trees.fit(x,y)
        print("model score: ",model.score(x,y))
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
        model=trees.fit(x_train,y_train)
        print("test score:",model.score(x_test,y_test))
        yEncoded=y
        xEncoded=df.drop('output',axis=1)
        decisionTree=tree.DecisionTreeClassifier(random_state=12345)
        decisionTree=decisionTree.fit(xEncoded,yEncoded)
        fig=tree.plot_tree(decisionTree,filled=True,rounded=True,class_names=["dangerous","normal"],feature_names=xEncoded.columns)
        plt.show()
    def randomForestClassifier(self):
        #it prevents overfitting via learning different random trees. result is 0 or 1
        file="heart.csv"
        data=pd.read_csv(file)
        df=pd.DataFrame(data)
        y=df['output']
        x=df.drop('output',axis=1)
        forest=RandomForestClassifier(n_estimators=200,max_depth=4) #n_estimator is trees count, max_depth is number of tree step
        model=forest.fit(x,y)
        print("model score: ",model.score(x,y))
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
        model=forest.fit(x_train,y_train)
        print("test score:",model.score(x_test,y_test))
    def boostingClassifier(self):
    #tree making new trees and improving itself by making new trees.    
        file="heart.csv"
        data=pd.read_csv(file)
        df=pd.DataFrame(data)
        y=df['output']
        x=df.drop('output',axis=1)   
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
        boost=xgb.XGBClassifier()
        model=boost.fit(x_train,y_train)
        print("test score: ",model.score(x_test,y_test))
    def randomForestRegressor(self): #result is changing not from 0-1. its unlimited.
        #reading files
        file="insurance.csv"
        data=pd.read_csv(file)
        df=pd.DataFrame(data)
        df=pd.get_dummies(df,columns=['sex','smoker','region'])
        y=df['charges']
        x=df.drop('charges',axis=1)
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
        rf=RandomForestRegressor(n_estimators=200)
        modelrf=rf.fit(x_train,y_train)
        print("random forest train score", modelrf.score(x_test,y_test))
        lr=LinearRegression()
        modelr=lr.fit(x_train,y_train)
        print("linear train score", modelr.score(x_test,y_test))
    def StandardScalerMinMaxScalerNormalize(self):
        #reading files
        file="Plane_Price.csv"
        data=pd.read_csv(file)
        df=pd.DataFrame(data)
        print(df.info(),"\n",df.describe(),"\n",df.columns)
        print(df.head(3))
        df=df[['Rcmnd cruise Knots', 'Stall Knots dirty',
       'Fuel gal/lbs', 'Eng out rate of climb', 'Price']].dropna()
        y=df['Price']
        x=df.drop(columns='Price')
        #normalize is not applying on Y-axis
        #normalize decreases outlier's effect and increases model's performance.
        #normalize makes std=0 and mean=1
        ss=StandardScaler()
        x2=ss.fit_transform(x)
        x2=pd.DataFrame(x2)
        print("std of columns",x2.std())
        print("mean of columns",x2.mean())
        mm=MinMaxScaler()
        x3=mm.fit_transform(x)
        x3=pd.DataFrame(x3)
        print(x3.max(),x3.min())
    def labelEncoder(self):
        #this makes string contens into numeric values.
        file="Tour_Winners_data_1.csv"
        data=pd.read_csv(file)
        df=pd.DataFrame(data)
        le=LabelEncoder()
        le.fit(df['Team'])
        df['Team']=le.transform(df['Team'])  
        print(le.classes_) 
        print(df['Team'])     
        

linearregressionmodels=LinearRegressionModels()
linearregressionmodels.labelEncoder()

    