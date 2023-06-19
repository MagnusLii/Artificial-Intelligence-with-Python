import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = load_diabetes(as_frame=True)

df = data.frame

sns.heatmap(data=df.corr().round(2), annot=True)
#The next variable I'd add would be "bp" because it has the next highest correlation with "target" while also having a lowish correlation with both "bmi" and "s5".
#plt.show()

plt.subplot(1,3,1)
plt.scatter(df['bmi'], df['target'])
plt.xlabel('bmi')
plt.ylabel('target')

plt.subplot(1,3,2)
plt.scatter(df['s5'], df['target'])
plt.xlabel('s5')
plt.ylabel('target')

plt.subplot(1,3,3)
plt.scatter(df['bp'], df['target'])
plt.xlabel('bp')
plt.ylabel('target')


X = pd.DataFrame(df[['bmi','s5', 'bp']], columns = ['bmi','s5', 'bp'])
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=5)
lm = LinearRegression()
lm.fit(X_train, y_train)

y_train_predict = lm.predict(X_train)
rmse = (np.sqrt(mean_squared_error(y_train, y_train_predict)))
r2 = r2_score(y_train, y_train_predict)

y_test_predict = lm.predict(X_test)
rmse_test = (np.sqrt(mean_squared_error(y_test, y_test_predict)))
r2_test = r2_score(y_test, y_test_predict)

print(rmse,r2)
print(rmse_test,r2_test)

#The performace is improved minutely.

#BMI, S5 and BP results.
#RMSE = 55.32610611166316  R2 = 0.47447150038132146
#Test RMSE = 56.6256100515053  test R2 = 0.4914938186648421

#BMI and S5 results.
#RMSE = 56.560890965481114, R2 = 0.4507519215172524
#RMSE (test) = 57.1759740950605, R2 (test)= 0.4815610845742896

# Adding a fourth variable increases R2 and decreases RMSE slightly again however the changes are still minute and for all intents and purposes may aswell be a rounding error.

X = pd.DataFrame(df[['bmi','s5', 'bp', 's3']], columns = ['bmi','s5', 'bp', 's3'])
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=5)
lm = LinearRegression()
lm.fit(X_train, y_train)

y_train_predict = lm.predict(X_train)
rmse = (np.sqrt(mean_squared_error(y_train, y_train_predict)))
r2 = r2_score(y_train, y_train_predict)

y_test_predict = lm.predict(X_test)
rmse_test = (np.sqrt(mean_squared_error(y_test, y_test_predict)))
r2_test = r2_score(y_test, y_test_predict)

print(rmse,r2)
print(rmse_test,r2_test)