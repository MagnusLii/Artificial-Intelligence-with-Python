

Consider the dataset from data_banknote_authentication.csv

0) Read data into a pandas dataframe.

1) Pick the column named "class" as target variable y and all other columns as feature variables X.

2) Split the data into training and testing sets with 80/20 ratio and random_state=20.

3) Use support vector classifier with linear kernel to fit to the training data.

4) Predict on the testing data and compute the confusion matrix and classification report.

5) Repeat steps 3 and 4 for the radial basis function kernel.

6) Compare the two SVM models in your own words.