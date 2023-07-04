import matplotlib.pyplot as plt
import pandas
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier

# 1) Read in the CSV file using pandas. Pay attention to the file delimeter.
df = pandas.read_csv("61_Problem_10_Banking_predictions/bank.csv", delimiter=";")

# 2) Pick data from the following columns to a second dataframe "df2": y, job, marital, default, housing, poutcome.
df2 = pandas.read_csv("61_Problem_10_Banking_predictions/bank.csv", delimiter=";", usecols=["y", "job", "marital", "default", "housing", "poutcome"])

# 3) Convert categorical variables to dummy numerical values using the command
df3 = pandas.get_dummies(df2, columns=["y", "job" ,"marital" ,"default" ,"housing" ,"poutcome"])

# 4) Produce a heat map of correlation coefficients for all variables in df3. Describe the amount of correlation between the variables in your own words.
seaborn.heatmap(df3.corr().round(2), annot=True)
plt.show()
# Most of the datapoints seems to have little to no correlation falling between +-0.0-0.1

# 5) Select the column called 'y' of df3 as the target variable y, and all the remaining columns for the explanatory variables X.
y = df3["y_yes"]
x = df3.drop(["y_yes", "y_no"], axis=1)

# 6) Split the dataset into training and testing sets with 75/25  ratio.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=5)

# 7) Setup a logistic regression model, train it with training data and predict on testing data.
logreg = LogisticRegression()
logreg.fit(x_train, y_train)
y_pred_logreg = logreg.predict(x_test)

# 8) Print the confusion matrix (or use heat map if you want) and accuracy score for the logistic regression model.
confusion = confusion_matrix(y_test, y_pred_logreg)
accuracy = accuracy_score(y_test, y_pred_logreg)

print("Confusion Matrix: \n", confusion)
print("Accuracy: ", accuracy)


# 9) Repeat steps 7 and 8 for k-nearest neighbors model. Use k=3, for example, or experiment with different values.
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(x_train, y_train)
y_pred_knn = knn.predict(x_test)

# 9) Repeat steps 7 and 8 for k-nearest neighbors model. Use k=3, for example, or experiment with different values.
knn_confusion = confusion_matrix(y_test, y_pred_knn)
knn_accuracy = accuracy_score(y_test, y_pred_knn)

# 10) Compare the results between the two models.
print("\n")
print("Kneighbour confusion matrix: \n", knn_confusion)
print("Kneighbour accuracy: ", knn_accuracy)