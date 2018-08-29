#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 04:18:20 2018

@author: Yigit

"""

#1. kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score
import statsmodels.api as sm

# Import Data
veriler = pd.read_csv('salaries.csv')

x = veriler.iloc[:,1:2]
y = veriler.iloc[:,2:]
X = x.values
Y = y.values

#Linear Regression
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,Y)

print('LR SCATTER')
plt.scatter(X,Y,color='red')
plt.plot(x,lin_reg.predict(X), color = 'blue')
plt.show()

print('LR OLS')
model = sm.OLS(lin_reg.predict(X),X)
print(model.fit().summary())

print("Linear R2 degeri:")
print(r2_score(Y, lin_reg.predict((X))))

#Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
x_poly = poly_reg.fit_transform(X)
print(x_poly)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)
print('POLY^2 SCATTER')
plt.scatter(X,Y,color = 'red')
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.show()

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(X)
print(x_poly)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly,y)
print('POLY^4 SCATTER')
plt.scatter(X,Y,color = 'red')
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.show()

#Predictions

print(lin_reg.predict(11))
print(lin_reg.predict(6.6))

print(lin_reg2.predict(poly_reg.fit_transform(11)))
print(lin_reg2.predict(poly_reg.fit_transform(6.6)))

print('Poly OLS')
model2 = sm.OLS(lin_reg2.predict(poly_reg.fit_transform(X)),X)
print(model2.fit().summary())

print("Polynomial R2 degeri:")
print(r2_score(Y, lin_reg2.predict(poly_reg.fit_transform(X)) ))

#Data Scaling
from sklearn.preprocessing import StandardScaler

sc1 = StandardScaler()
x_olcekli = sc1.fit_transform(X)
sc2 = StandardScaler()
y_olcekli = sc2.fit_transform(Y)

from sklearn.svm import SVR

svr_reg = SVR(kernel = 'rbf')
svr_reg.fit(x_olcekli,y_olcekli)

print('SVR SCATTER')
plt.scatter(x_olcekli,y_olcekli,color='red')
plt.plot(x_olcekli,svr_reg.predict(x_olcekli),color='blue')
plt.show()
print(svr_reg.predict(11))
print(svr_reg.predict(6.6))

print('SVR OLS')
model3 = sm.OLS(svr_reg.predict(x_olcekli),x_olcekli)
print(model3.fit().summary())

print("SVR R2 degeri:")
print(r2_score(y_olcekli, svr_reg.predict(x_olcekli)) )


#Decision Tree Regression
from sklearn.tree import DecisionTreeRegressor
r_dt = DecisionTreeRegressor(random_state=0)
r_dt.fit(X,Y)
Z = X + 0.5
K = X - 0.4
print('DT SCATTER')
plt.scatter(X,Y, color='red')
plt.plot(x,r_dt.predict(X), color='blue')
plt.plot(x,r_dt.predict(Z),color='green')
plt.plot(x,r_dt.predict(K), color = 'yellow')
plt.show()
print(r_dt.predict(11))
print(r_dt.predict(6.6))

print('DT OLS')
model4 = sm.OLS(r_dt.predict(X),X)
print(model4.fit().summary())

print("Decision Tree R2 degeri:")
print(r2_score(Y, r_dt.predict(X)) )

#Random Forest Regression
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators = 10, random_state=0)
rf_reg.fit(X,Y)

print(rf_reg.predict(6.6))
print('RF SCATTER')
plt.scatter(X,Y, color='red')
plt.plot(x,rf_reg.predict(X), color = 'blue')
plt.plot(x,rf_reg.predict(Z), color = 'green')
plt.plot(x,r_dt.predict(K), color = 'yellow')
plt.show()

print('RF OLS')
model5 = sm.OLS(rf_reg.predict(X),X)
print(model5.fit().summary())


print("Random Forest R2 degeri:")
print(r2_score(Y, rf_reg.predict(X)) )
print(r2_score(Y, rf_reg.predict(K)) )
print(r2_score(Y, rf_reg.predict(Z)) )

#R2 Scores - Summary
print('----------------')
print("Linear R2 degeri:")
print(r2_score(Y, lin_reg.predict((X))))

print("Polynomial R2 degeri:")
print(r2_score(Y, lin_reg2.predict(poly_reg.fit_transform(X)) ))

print("SVR R2 degeri:")
print(r2_score(y_olcekli, svr_reg.predict(x_olcekli)) )

print("Decision Tree R2 degeri:")
print(r2_score(Y, r_dt.predict(X)) )

print("Random Forest R2 degeri:")
print(r2_score(Y, rf_reg.predict(X)) )




