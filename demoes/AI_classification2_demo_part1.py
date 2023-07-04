
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix

df2 = pd.read_csv("demoes\iris.csv")
print(df2.head())

X = df2.drop('species', axis=1)
y = df2['species']
print(X,y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20,random_state=20)
print(X_train.shape,X_test.shape)

svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)
y_pred = svclassifier.predict(X_test)

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

svclassifier = SVC(kernel='poly', degree=2)
svclassifier.fit(X_train, y_train)
y_pred = svclassifier.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

svclassifier = SVC(kernel='rbf')
svclassifier.fit(X_train, y_train)
y_pred = svclassifier.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

print("column 0 =",df2.iloc[:,0])
print("columns 0,1 =",df2.iloc[:,[0,1]])
