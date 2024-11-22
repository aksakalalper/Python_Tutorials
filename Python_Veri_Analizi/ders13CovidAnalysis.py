import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from seaborn import heatmap
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPRegressor

import matplotlib.pyplot as plt

plt.style.use('ggplot')

file='tr_covid_en.csv'
data=pd.read_csv(file,sep=';',index_col=0)
df=pd.DataFrame(data=data)
print(df.head(5),"\n",df.describe())
print(df.info())

print(df.isna().sum())
df.index=pd.to_datetime(df.index,format='%d.%m.%Y')
df = df.drop(df.index[0:9])

scaler=MinMaxScaler()
df_scaled=pd.DataFrame(scaler.fit_transform(df),columns=df.columns)
df_scaled=pd.DataFrame(df_scaled,columns=df.columns)
df_scaled.index=df.index
print(df_scaled.head())
corr=df_scaled.corr()
heatmap(corr,xticklabels=df.columns,yticklabels=df.columns)
plt.show()