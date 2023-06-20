Consider car performance data from the file Auto.csv.

1) Read the data into pandas dataframe

2) Setup multiple regression X and y to predict 'mpg' of cars using all the variables except 'mpg', 'name' and 'origin'

3) Split data into training and testing sets (80/20 split)

4) Implement both ridge regression and LASSO regression using several values for alpha

5) Search optimal value for alpha (in terms of R2 score) by fitting the models with training data and computing the score using testing data

6) Plot the R2 scores for both regressors as functions of alpha

7) Identify, as accurately as you can, the value for alpha which gives the best score

 

Include your own findings and explanations in code comments or inside triple quotes """...""".