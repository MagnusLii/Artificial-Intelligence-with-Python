import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split

df = pd.read_csv("demoes\exams.csv",skiprows=0,delimiter=",")
print(df)

X = df.iloc[:, 0:2]
y = df.iloc[:, -1]
print("X=",X)
print("y=",y)

admit_yes = df.loc[y == 1]
admit_no  = df.loc[y == 0]
print(admit_no)

plt.scatter(admit_no.iloc[:,0],admit_no.iloc[:,1],label="admit no")
plt.scatter(admit_yes.iloc[:,0],admit_yes.iloc[:,1],label="admit yes")
plt.xlabel("exam1")
plt.ylabel("exam2")
plt.legend()
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25,random_state=0)
print(X_train.shape)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

metrics.ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
plt.show()
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print(cnf_matrix)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred))
print("Recall:",metrics.recall_score(y_test, y_pred))


y_test2 = y_test.to_numpy()

idx1 = np.logical_and(y_pred == 1, y_test2 == 1)
idx2 = np.logical_and(y_pred == 1, y_test2 == 0)
idx3 = np.logical_and(y_pred == 0, y_test2 == 0)
idx4 = np.logical_and(y_pred == 0, y_test2 == 1)
X1 = X_test.loc[idx1]
X2 = X_test.loc[idx2]
X3 = X_test.loc[idx3]
X4 = X_test.loc[idx4]

plt.scatter(X1.iloc[:,0],X1.iloc[:,1],label="pred yes correct",marker="+",color="blue")
plt.scatter(X2.iloc[:,0],X2.iloc[:,1],label="pred yes incorrect",marker="o",color="blue")
plt.scatter(X3.iloc[:,0],X3.iloc[:,1],label="pred no correct",marker="+",color="red")
plt.scatter(X4.iloc[:,0],X4.iloc[:,1],label="pred yes incorrect",marker="o",color="red")
plt.xlabel("exam1")
plt.ylabel("exam2")
plt.legend()
plt.title("Predicted")
plt.show()
