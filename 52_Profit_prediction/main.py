import numpy
import matplotlib.pyplot as plt
import pandas
import seaborn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Read the dataset into pandas dataframe paying attention to file delimeter.
df = pandas.read_csv("52_Profit_prediction/50_Startups.csv", delimiter=",", usecols=["R&D Spend", "Administration", "Marketing Spend", "Profit"])

# Identify the variables inside the dataset
#print(df)

# Investigation of correlation of variables to profit.
seaborn.heatmap(data=df.corr(), annot=True)
#plt.show()

#Choose appropriate variables to predict company profit. Justify your choice.
# R&D and marketing spending seem to be highly correlated to profits while not being too correlated to eachother.

# Plot explanatory variables against profit in order to confirm (close to) linear dependence
plt.subplot(1,2,1)
plt.scatter(df["R&D Spend"], df["Profit"])
plt.xlabel("R&D Spend")
plt.ylabel("Profit")

# marketing spending dependence is not perfectly linear but close enough.
plt.subplot(1,2,2)
plt.scatter(df["Marketing Spend"], df["Profit"])
plt.xlabel("Marketing Spend")
plt.ylabel("Profit")
plt.show()

X = pandas.DataFrame(df[["R&D Spend","Marketing Spend"]], columns = ["R&D Spend","Marketing Spend"])
y = df["Profit"]
# Form training and testing data (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 5)

# Train linear regression model with training data
lm = LinearRegression()
lm.fit(X_train, y_train)

# Compute RMSE and R2 values for training and testing data separately
y_train_predict = lm.predict(X_train)
RMSE = (numpy.sqrt(mean_squared_error(y_train, y_train_predict)))
R2 = r2_score(y_train, y_train_predict)

y_test_predict = lm.predict(X_test)
RMSE_test = (numpy.sqrt(mean_squared_error(y_test, y_test_predict)))
R2_test = r2_score(y_test, y_test_predict)

print(f"RMSE: {RMSE}, R2: {R2}")
print(f"RMSE_test: {RMSE_test}, R2_test: {R2_test}")