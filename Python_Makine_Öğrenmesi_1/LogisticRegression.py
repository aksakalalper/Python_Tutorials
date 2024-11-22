import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.model_selection import GridSearchCV

# Load data
fileTrain = "train.csv"
fileTest = "test.csv"
dataTrain = pd.read_csv(fileTrain)
dataTest = pd.read_csv(fileTest)

# Data preprocessing
dfTrain = pd.DataFrame(dataTrain)
dfTest = pd.DataFrame(dataTest)

# Fill missing values for Age and Embarked in train data
dfTrain['Age'].fillna(dfTrain['Age'].mean(), inplace=True)
dfTrain['Embarked'].fillna(dfTrain['Embarked'].value_counts().idxmax(), inplace=True)

# Drop unnecessary columns
dfTrain.drop(['Cabin', 'SibSp', 'Parch', 'PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)

# Fill missing values for Age and Fare in test data
dfTest['Age'].fillna(dfTest['Age'].mean(), inplace=True)
dfTest['Fare'].fillna(dfTest['Fare'].median(), inplace=True)

# Drop unnecessary columns in test data
dfTest.drop(['SibSp', 'Parch', 'Name', 'Cabin', 'Ticket'], axis=1, inplace=True)

# Encode categorical variables using get_dummies (one-hot encoding)
training = pd.get_dummies(dfTrain, columns=['Pclass', 'Embarked', 'Sex'])
testing = pd.get_dummies(dfTest, columns=['Pclass', 'Embarked', 'Sex'])

# Align test and train datasets by reindexing test data
testing = testing.reindex(columns=training.columns, fill_value=0)

# Define features and target variable for training
cols = ['Age', 'Fare', 'Pclass_1', 'Pclass_2', 'Pclass_3', 'Embarked_C', 'Embarked_Q', 'Embarked_S', 'Sex_female', 'Sex_male']
x = training[cols]
y = dfTrain['Survived']

# Initialize and fit the logistic regression model with RFE
model = LogisticRegression(max_iter=200)
rfe = RFE(model, n_features_to_select=5)
rfe = rfe.fit(x, y)

# Output selected features
print("Selected features:", x.columns[rfe.support_])

xx = training[x.columns[rfe.support_]]
yy = training['Survived']

# Define the parameter grid
param_grid = {'C': np.arange(0.0005, 3, 0.1), 'penalty': ['l1', 'l2']}
scoring = {'Accuracy': 'accuracy'}

# Initialize GridSearchCV
gs = GridSearchCV(LogisticRegression(solver='liblinear'), return_train_score=True, param_grid=param_grid, scoring=scoring, cv=10, refit='Accuracy')

# Fit GridSearchCV
gs.fit(xx, yy)

# Output the results
results = gs.cv_results_
print('En iyi parametreler:', gs.best_estimator_)
print('Optimum hiperparametre:', gs.best_params_)
print('En iyi skor:', gs.best_score_)
