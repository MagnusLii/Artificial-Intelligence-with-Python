import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("winequality-white.csv",delimiter=";")
print(df.head())

sns.heatmap(data=df.corr().round(2).abs(), annot=True)
plt.show()

plt.subplot(1,2,1)
plt.scatter(df['residual sugar'],df['density'])
plt.xlabel("residual sugar")
plt.ylabel("density")

plt.subplot(1,2,2)
plt.scatter(df['alcohol'],df['density'])
plt.xlabel("alcohol")
plt.ylabel("density")
plt.show()

X = pd.DataFrame(df[['residual sugar','alcohol']])
y = df['density']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=5)

print(X_train.shape)
print(X_test.shape)

lm = LinearRegression()
lm.fit(X_train, y_train)

y_train_predict = lm.predict(X_train)
rmse = (np.sqrt(mean_squared_error(y_train, y_train_predict)))
r2 = r2_score(y_train, y_train_predict)

y_test_predict = lm.predict(X_test)
rmse_test = (np.sqrt(mean_squared_error(y_test, y_test_predict)))
r2_test = r2_score(y_test, y_test_predict)

print("RMSE=",rmse,"R2=",r2)
print("RMSE (test)=",rmse_test,"R2 (test)=",r2_test)
