import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import  yfinance as yf
from sklearn.metrics import mean_squared_error

# veri seti yüklenir
ticker="USDTRY=X"
data=yf.download(f'{ticker}','2022-01-01','2024-11-01')
print(data.head(10))
data.to_csv(f'{ticker}.csv')
file=f'{ticker}.csv'
dt=pd.read_csv(file)
df=pd.DataFrame(dt)
print(df.info(),df.describe(),df.columns,df.index)
print(df.head(10))
df = df.drop([0,1])
print(df.head(10))
df.to_csv('cleanData.csv')

file='cleanData.csv'
data=pd.read_csv(file)
df=pd.DataFrame(data)
# kur kazancı için sütun oluşturuldu.
df['Return']=df.Close.diff()
#dönem boyunca pozitif ve negatif getiri.
print(sum(i for i in df['Return'] if i>0))
print(sum(i for i in df['Return'] if i<0))
print(df['Return'].min())
print(df['Return'].max())
print(df['Return'].std())

# grafiğe dökülür. kapanış değeri durağan olmayan bir seriyken kur farkı durağan seridir.
f=plt.figure(figsize=(20,12))
f.suptitle('Dolar/TL kapanış ve kur değişimi')
plt.subplot(211)
plt.grid()
plt.plot(df['Close'])
plt.subplot(212)
plt.plot(df['Return'],'r')
plt.grid()
plt.show()
# aykırı değer tespiti yapılır.
print(f'gözlem sayısı {len(df)} şlem günü')
print(df.head(5))

