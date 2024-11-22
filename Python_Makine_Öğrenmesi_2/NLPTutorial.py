from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble  import RandomForestClassifier
from sklearn.model_selection  import train_test_split,cross_val_score,KFold
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from pmdarima import model_selection
import pmdarima as pm
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

class NLPTutorial():
    def __init__(self):
        pass
    def countVectorizer(self):
        #this method makes contents into numeric values. it makes matrix and vector
        #and also this one using in natural language models.
        df=pd.DataFrame()
        df['text']=['car bird car','car car bird','car bus bird','truck motor bicycle']
        cv=CountVectorizer(max_features=2) #this parameter highlights top 2 words
        out=cv.fit_transform(df['text'])
        print(out.toarray())
        print(cv.get_feature_names_out()) #most common top 2 words
        #stop words are words that we don't need to count
    def NLPMobileBankApp(self):
        file="banka.csv"
        data=pd.read_csv(file)
        df=pd.DataFrame(data)
        print(df.info(),"\n",df.describe(),"\n",df.columns)
        df=df.drop(columns=['Unnamed: 0','le'])
        with open('turkce-stop-words.txt', 'r', encoding='utf-8') as f:
            words = f.read().splitlines()
        word_list = [word for word in words]
        for word in word_list:
            word=" "+ word +" "
            df['sorgu']=df['sorgu'].str.replace(word," ",regex=False)
        cv=CountVectorizer(max_features=50)
        x=cv.fit_transform(df['sorgu'])
        y=df['label']
        print(x.toarray())
        print(cv.get_feature_names_out())
        rf=RandomForestClassifier()
        model=rf.fit(x,y)
        print("model score",model.score(x,y))
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
        modelrf=rf.fit(x_train,y_train)
        print("train score", modelrf.score(x_test,y_test))
        userMessage = input("Enter your message: ") 
        message_transformed = cv.transform([userMessage]) 
        prediction = model.predict(message_transformed) 
        print(f"Result: {prediction[0]}")
    def oneHotEncoding(self):
        #this methos makes converts column values into binary.
        file="Churn_Modelling.csv"
        data=pd.read_csv(file)
        df=pd.DataFrame(data)
        df=df.drop(columns=['RowNumber','CustomerId','Surname'])
        ohe=OneHotEncoder()
        encodedColumns=ohe.fit_transform(df[['Gender','Geography']]).toarray()
        df=df.drop(columns=['Gender','Geography'])
        dfEncoded=pd.DataFrame(encodedColumns,columns=['Gender_Male','Gender_Female','Geography_France','Geography_Germany','Geography_Spain'])
        df=pd.concat([df, dfEncoded], axis=1)
        y=df['Exited']
        x=df.drop('Exited',axis=1)
        dtc=DecisionTreeClassifier()
        model=dtc.fit(x,y)
        print("model score",model.score(x,y))
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
        modeldtc=dtc.fit(x_train,y_train)
        print("train score", modeldtc.score(x_test,y_test)) #overfitting situation
    def timeSeriesForecasting(self):
        #selecting global gold price
        ticker='GC=F'
        #df = yf.download(ticker, period='2y')
        #df.to_csv('gold_price.csv')
        file = "gold_price.csv"
        data = pd.read_csv(file)
        df = pd.DataFrame(data)
        df = df.drop(columns=['High', 'Low', 'Adj Close', 'Open', 'Volume'])
        df = df.iloc[2:] 
        df.columns = ['Date', 'Price']
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
        df['Price'] = df['Price'].astype(float).round(2)
        train, test = train_test_split(df, test_size=0.3, shuffle=False)
        model = pm.auto_arima(train,start_p=1,
                                     start_q=1,
                                     test="adf",
                                     d=1,
                                     seasonal = False,
                                     error_action = 'ignore',
                                     suppress_warnings=True,
                                     trace=True)
        preds, conf_int = model.predict(n_periods=test.shape[0], return_conf_int=True)
        plt.figure(figsize=(10, 6))
        plt.plot(train.index, train['Price'], label='Eğitim Verisi')
        plt.plot(test.index, test['Price'], label='Gerçek Değerler')
        plt.plot(test.index, preds, label='Tahminler')
        plt.fill_between(test.index, conf_int[:, 0], conf_int[:, 1], color='blue', alpha=0.1)
        plt.title("Altın Fiyatları Tahmini")
        plt.xlabel("Tarih")
        plt.ylabel("Fiyat")
        plt.legend()
        plt.show()
    def crossValScore(self):
        #cross validation divides data to cvfolds. 
        # it's used for model evaluation.
        # every time model trains with different data.
        file="customer_booking.csv"
        data=pd.read_csv(file,encoding='latin-1')
        df=pd.DataFrame(data)
        print(df.drop_duplicates(keep='first',inplace=True))
        print(df.head(5))
        le = LabelEncoder()
        le.fit(df['flight_day'])
        df['flight_day'] = le.transform(df['flight_day'])
        le.fit(df['sales_channel'])
        df['sales_channel'] = le.transform(df['sales_channel'])
        le.fit(df['trip_type'])
        df['trip_type'] = le.transform(df['trip_type'])
        le.fit(df['flight_day'])
        df['flight_day'] = le.transform(df['flight_day'])
        le.fit(df['route'])
        df['route'] = le.transform(df['route'])
        le.fit(df['booking_origin'])
        df['booking_origin'] = le.transform(df['booking_origin'])
        print(df.head(5))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', square=True,annot_kws={'size': 8})
        #plt.show()
        #print(le.classes_)
        #print(le.transform(le.classes_))
        y=df['wants_extra_baggage']
        x=df.drop('wants_extra_baggage',axis=1)
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
        rfc=RandomForestClassifier()
        model=rfc.fit(x_train,y_train)
        print("model score",model.score(x_train,y_train))
        print("test score",model.score(x_test,y_test))
        kf = KFold(n_splits=5, shuffle=True, random_state=42)
        print(cross_val_score(rfc,x,y,cv=kf).mean())


nlptutorial=NLPTutorial()
nlptutorial.crossValScore()
    


