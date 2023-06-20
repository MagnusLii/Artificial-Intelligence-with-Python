
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weight-height.csv")
print(df.head())

print(df.corr())

plt.scatter(df['Weight'],df['Height'])
plt.xlabel("Weight")
plt.ylabel("Height")
plt.show()
