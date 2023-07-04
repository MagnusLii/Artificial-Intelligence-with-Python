import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report



# Read data into a pandas dataframe.
df = pandas.read_csv("73_Decision_tree\suv.csv", delimiter=",")

# Pick Age and Estimated Salary as the features and Purchased as the target variable.
x = df[["Age", "EstimatedSalary"]]
y = df["Purchased"]

# Split the data into training and testing sets with 80/20 ratio.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=5)

# Scale the features using standard scaler.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(x_train)
X_test_scaled = scaler.transform(x_test)

# Train a decision tree classifier with entropy criterion and predict on test set.
clf_entropy = DecisionTreeClassifier(criterion="entropy")
clf_entropy.fit(X_train_scaled, y_train)
y_pred_entropy = clf_entropy.predict(X_test_scaled)

# Print the confusion matrix and the classification report.
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_entropy))
print("\nClassification Report:")
print(classification_report(y_test, y_pred_entropy))

# Repeat steps 4 and 5 with the gini criterion.
clf_gini = DecisionTreeClassifier(criterion="gini")
clf_gini.fit(X_train_scaled, y_train)
y_pred_gini = clf_gini.predict(X_test_scaled)
print("\n")

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred_gini))
print("\nClassification Report:")
print(classification_report(y_test, y_pred_gini))
