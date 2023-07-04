
import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd
import numpy as np

df = pd.read_csv('demoes\Admission_Predict.csv',skiprows=0,delimiter=",")
print(df.head())

X = df[["CGPA",'GRE Score']]
y = df[["Chance of Admit "]]
print(X)
print(y)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=30)

X_train_norm = MinMaxScaler().fit_transform(X_train)
X_test_norm = MinMaxScaler().fit_transform(X_test)
X_train_std = StandardScaler().fit_transform(X_train)
X_test_std = StandardScaler().fit_transform(X_test)
print(X_train_norm[:10])
#print(X_test_norm)
#print(X_train_std)
print(X_test_std[:10])

lm = neighbors.KNeighborsRegressor(n_neighbors=5)
lm.fit(X_train, y_train)
predictions = lm.predict(X_test)
print("R2 =",lm.score(X_test,y_test))

lm.fit(X_train_norm, y_train)
print("R2 (norm) =",lm.score(X_test_norm,y_test))

lm.fit(X_train_std, y_train)
print("R2 (std) =",lm.score(X_test_std,y_test))

plt.hist(np.array(X[['CGPA']]),20)
plt.xlabel("CGPA")
plt.show()
plt.hist(np.array(X[['GRE Score']]),20)
plt.xlabel("GRE Score")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(np.array(X_test[['CGPA']]),np.array(X_test[['GRE Score']]),predictions)
ax.set_xlabel('CGPA')
ax.set_ylabel('GRE Score')
ax.set_zlabel('Chance of Admit')
plt.show()
