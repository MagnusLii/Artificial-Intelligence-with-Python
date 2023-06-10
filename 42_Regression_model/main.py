import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model


def sklearn():
    #my_data = np.genfromtxt("weight-height(1).csv", delimiter=',')
    xp = np.genfromtxt("weight-height(1).csv", delimiter=",", dtype=float, skip_header=1, usecols=2)
    yp = np.genfromtxt("weight-height(1).csv", delimiter=",", dtype=float, skip_header=1, usecols=1)
    xp = xp.reshape(-1,1)
    yp = yp.reshape(-1,1)

    regr = linear_model.LinearRegression()
    regr.fit(xp, yp) # fitting the model=training the model

    print(regr.coef_,regr.intercept_)

    xval = np.full((1,1),0.5)
    yval = regr.predict(xval)
    print(yval)

    xval = np.linspace(-1,2,20).reshape(-1,1)
    yval = regr.predict(xval)
    plt.plot(xval,yval) # this plots the line
    plt.scatter(xp,yp,color="red")
    plt.show()

    from sklearn import metrics
    yhat = regr.predict(xp)
    print('Mean Absolute Error:', metrics.mean_absolute_error(yp, yhat))  
    print('Mean Squared Error:', metrics.mean_squared_error(yp, yhat))  
    print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(yp, yhat)))
    print('R2 value:', metrics.r2_score(yp, yhat))


weight = np.genfromtxt("weight-height(1).csv", delimiter=",", dtype=float, skip_header=1, usecols=2)
height = np.genfromtxt("weight-height(1).csv", delimiter=",", dtype=float, skip_header=1, usecols=1)

n = weight.size
xbar = np.mean(weight)
ybar = np.mean(height)

term1 = np.sum(weight*height)
term2 = np.sum(weight**2)

b = (term1-n*xbar*ybar)/(term2-n*xbar*xbar)
a = ybar - b*xbar

x = np.linspace(min(height), max(weight),100)
y = a+b*x

yhat = a+b*weight
RSS = np.sum((height-yhat)**2)
print("RSS =",RSS)
RMSE = np.sqrt(np.sum((height-yhat)**2)/n)
print("RMSE=",RMSE)
MAE = np.sum(np.abs(height-yhat))/n
print("MAE =",MAE)
MSE = np.sum((height-yhat)**2)/n
print("MSE =",MSE)
R2 = 1-np.sum((height-yhat)**2)/np.sum((height-ybar)**2)
print("R2  =",R2)

plt.plot(x, y, color="black")
plt.scatter(weight, height)
plt.scatter(xbar, ybar, color="red")
plt.xlabel("weight")
plt.ylabel("height")
plt.show()
print("----------------------------------------------------------------------")

sklearn()
