Consider the data from CSV file weight-height.csv.

0) Read data into a pandas dataframe.

1) Pick the target variable y as weight in kilograms, and the feature variable X as height in centimeters.

2) Split the data into training and testing sets with 80/20 ratio.

3) Scale the training and testing data using normalization and standardization.

4) Fit a KNN regression model with k=5 to the training data without scaling, predict on unscaled testing data and compute the R2 value.

5) Repeat step 4 for normalized data.

6) Repeat step 4 for standardize data.

7) Compare the models in terms of their R2 value.