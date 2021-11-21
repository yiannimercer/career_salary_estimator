#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 20:55:23 2021

@author: yiannimercer
"""

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("eda_data.csv")

# Choose our relevant columns

df.columns


df_model = df[['avg_salary','Rating','Size','Type of ownership','Industry','Sector','Revenue','employer_provided','job_state','age',
               'simplified_job_title','seniority']]

# Get Dummy Data
df_dum = pd.get_dummies(df_model)

df_model.info()
# Train-Test Split

from sklearn.model_selection import train_test_split

X = df_dum.drop('avg_salary',axis = 1)
y = df_dum.avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 111)

# Multiple Linear Regression
from sklearn.linear_model import LinearRegression, Lasso 
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train, y_train)

lm_cv = cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 5)
np.mean(lm_cv)

plt.plot(range(1,6),lm_cv,marker ='o')
plt.title("Multiple Linear Regression Performance on 5-Fold CV")
plt.xlabel("K-Fold")
plt.ylabel("Negative Mean Absolute Error")


# lasso regression 
lm_l = Lasso(0.01) # Alpha value added after iterating through various alpha values
lm_l.fit(X_train,y_train)
np.mean(cross_val_score(lm_l,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 5))

alpha = []
error = []

for i in range(1,100):
    alpha.append(i/100)
    lml = Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lml,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 5)))
    
plt.plot(alpha,error)
plt.title("Average Negative Mean Absolute Error for Each Alpha Parameter of LASSO Regression")
plt.xlabel("Alpha")
plt.ylabel("Error")

err = tuple(zip(alpha,error))
df_err = pd.DataFrame(err, columns = ['alpha','error'])
df_err[df_err.error == max(df_err.error)]

# random forest 
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(random_state=42)

rf_cv = cross_val_score(rf,X_train,y_train,scoring = 'neg_mean_absolute_error', cv= 5)

plt.plot(range(1,6),rf_cv,marker ='o')
plt.title("Random Forest Regression Performance on 5-Fold CV")
plt.xlabel("K-Fold")
plt.ylabel("Negative Mean Absolute Error")

# tune models GridsearchCV 
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,300,60), 'criterion':['mse'], 'max_features':('auto','sqrt')}

gs = GridSearchCV(rf,parameters,scoring='neg_mean_absolute_error',cv=3, n_jobs=-1)
gs.fit(X_train,y_train)

gs.best_score_
gs.best_estimator_

# test ensembles 
tpred_lm = lm.predict(X_test)
tpred_lml = lm_l.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test,tpred_lm)
mean_absolute_error(y_test,tpred_lml)
mean_absolute_error(y_test,tpred_rf)

# saving the model 
import pickle 
pickle_out = open("regressor.pkl", mode = "wb") 
pickle.dump(gs.best_estimator_, pickle_out) 
pickle_out.close()
