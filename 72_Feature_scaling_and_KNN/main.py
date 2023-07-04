import pandas
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Read data into a pandas dataframe.
df = pandas.read_csv("72_Feature_scaling_and_KNN\weight-height.csv", delimiter=",")

# Pick the target variable y as weight in kilograms, and the feature variable X as height in centimeters.
x = (df["Height"] * 2.54).values.reshape(-1, 1)
y = (df["Weight"] * 0.453592).values

# Split the data into training and testing sets with 80/20 ratio.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=20)

# Scale the training and testing data using normalization and standardization.
# normalization
normalizer = MinMaxScaler()
x_train_normalized = normalizer.fit_transform(x_train)
x_test_normalized = normalizer.transform(x_test)

# standardization
standardizer = StandardScaler()
x_train_standardized = standardizer.fit_transform(x_train)
X_test_standardized = standardizer.transform(x_test)

# Fit a KNN regression model with k=5 to the training data without scaling, predict on unscaled testing data and compute the R2 value.
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(x_train, y_train)
y_pred_unscaled = knn.predict(x_test)
r2_unscaled = r2_score(y_test, y_pred_unscaled)

#  Repeat step 4 for normalized data.
knn_normalized = KNeighborsRegressor(n_neighbors=5)
knn_normalized.fit(x_train_normalized, y_train)
y_pred_normalized = knn_normalized.predict(x_test_normalized)
r2_normalized = r2_score(y_test, y_pred_normalized)

#  Repeat step 4 for standardized data.
knn_standardized = KNeighborsRegressor(n_neighbors=5)
knn_standardized.fit(x_train_standardized, y_train)
y_pred_standardized = knn_standardized.predict(X_test_standardized)
r2_standardized = r2_score(y_test, y_pred_standardized)

# Compare the models in terms of their R2 value.
print(f"R2 unscaled: {r2_unscaled}")
print(f"R2 normalized: {r2_normalized}")
print(f"R2 standardized: {r2_standardized}")