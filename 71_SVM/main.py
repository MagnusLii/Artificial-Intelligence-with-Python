import pandas
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report

# Read data into a pandas dataframe.
df = pandas.read_csv("71_SVM\data_banknote_authentication.csv", delimiter=",")

# Pick the column named "class" as target variable y and all other columns as feature variables X.
x = df.drop("class", axis=1)
y = df["class"]

# Split the data into training and testing sets with 80/20 ratio and random_state=20.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=20)

# Use support vector classifier with linear kernel to fit to the training data.
svm_linear = SVC(kernel="linear")
svm_linear.fit(x_train, y_train)

# Predict on the testing data and compute the confusion matrix and classification report.
y_pred_linear = svm_linear.predict(x_test)
confusion_linear = confusion_matrix(y_test, y_pred_linear)
classification_report_linear = classification_report(y_test, y_pred_linear)

print("Confusion Matrix (Linear Kernel):\n", confusion_linear)
print("\n")
print("Classification Report (Linear Kernel):\n", classification_report_linear)

# Repeat steps 3 and 4 for the radial basis function kernel.
svclassifier = SVC(kernel="rbf")
svclassifier.fit(x_train, y_train)
y_pred = svclassifier.predict(x_test)

print(confusion_matrix(y_test, y_pred))
print("\n")
print(classification_report(y_test, y_pred))