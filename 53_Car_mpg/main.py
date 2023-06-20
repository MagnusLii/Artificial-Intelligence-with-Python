import numpy
import matplotlib.pyplot as plt
import pandas
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge, Lasso

# Task 1: Read the data into pandas dataframe
df = pandas.read_csv("53_Car_mpg\Auto.csv")
columns = ["cylinders", "displacement", "horsepower", "weight", "acceleration", "year"] #TODO Obsolete! Delete later.


# Task 2: Setup multiple regression X and y
x = df.drop(["mpg", "name", "origin"], axis=1)
y = df["mpg"]

# Task 3: Split data into training and testing sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 5)

# Task 4: Implement both ridge regression and LASSO regression using several values for alpha
alphas = numpy.linspace(0, 1000, 50)
ridge_scores = []
lasso_scores = []

for alpha in alphas:
    # ridge Regression
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train, y_train)
    ridge_pred = ridge.predict(X_test)
    ridge_scores.append(r2_score(y_test, ridge_pred))

    # lasso Regression
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    lasso_pred = lasso.predict(X_test)
    lasso_scores.append(r2_score(y_test, lasso_pred))

# Task 5: Search optimal value for alpha (in terms of R2 score)
best_alpha_ridge = alphas[numpy.argmax(ridge_scores)]
best_alpha_lasso = alphas[numpy.argmax(lasso_scores)]

# Task 6: Plot the R2 scores for both regressors as functions of alpha
plt.plot(alphas, ridge_scores, label="Ridge Regression")
plt.plot(alphas, lasso_scores, label="LASSO Regression")
plt.xlabel("Alpha")
plt.ylabel("R2 Score")
plt.title("R2 Scores for Ridge and LASSO Regression")
plt.show()

# Task 7: Identify the value for alpha which gives the best score
print("\n\n\n\n\n")
print(f"The best alpha value for Ridge Regression: {best_alpha_ridge}")
print(f"The best alpha value for LASSO Regression: {best_alpha_lasso}")
print("\n\n\n\n\n")