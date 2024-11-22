import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.linear_model import LinearRegression, BayesianRidge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR

# Verileri okuma
file = "SATILIK_EV1.xlsx"
data = pd.read_excel(file)
df = pd.DataFrame(data)

# Axis ayarlama ve gereksiz sütunu kaldırma
df = df.drop('Unnamed: 0', axis=1)
print(df.head(5))

# Hedef değişken ve özellikler
y = df['Fiyat']
x = df.drop('Fiyat', axis=1)

# Eğitim ve test setlerine ayırma
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Modelleri ve değerlendirme listelerini tanımlama
models = [
    LinearRegression(),
    KNeighborsRegressor(n_neighbors=3),
    BayesianRidge(),
    DecisionTreeRegressor(),
    SVR(kernel='linear')
]

cv_results = []
cv_means = []
cv_std = []

# 10 katlı çapraz doğrulama
kfold = KFold(n_splits=10, random_state=42, shuffle=True)

for model in models:
    cv_result = cross_val_score(model, x_train, y_train, scoring='neg_root_mean_squared_error', cv=kfold, n_jobs=-1)
    cv_results.append(cv_result)
    cv_means.append(cv_result.mean())
    cv_std.append(cv_result.std())

cv_frame = pd.DataFrame({
    'CrossValMeans': cv_means,
    'CrossValScore': cv_std,
    'Algorithms': ['LinearRegression', 'KNeighborsRegressor', 'BayesianRidge', 'DecisionTreeRegressor', 'SVR']
})

# Çapraz doğrulama sonuçlarını görselleştirme
cv_plot = sns.barplot(x='CrossValMeans', y='Algorithms', data=cv_frame, palette='husl', orient='h')
cv_plot.set_xlabel('RMSE skorları')
cv_plot.set_title('Çapraz Doğrulama Skorları')
plt.show()

final=KNeighborsRegressor(n_neighbors=3)
final=final.fit(x_train,y_train)

y_pred_test=final.predict(x_test)
y_pred_train=final.predict(x_train)

from sklearn.metrics import r2_score,mean_squared_error
print("eğitim seti için rmse",np.sqrt(mean_squared_error(y_train,y_pred_train)))
print("test seti için rmse",np.sqrt(mean_squared_error(y_test,y_pred_test)))
print("eğitim seti için rmse",np.sqrt(r2_score(y_train,y_pred_train)))
print("test seti için rmse",np.sqrt(r2_score(y_test,y_pred_test)))