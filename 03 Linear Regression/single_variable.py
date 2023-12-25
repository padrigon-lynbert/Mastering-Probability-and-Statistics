import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv("DataCSV\\LinearRegression\\home_prices.csv")
# print(df)

# plt.scatter(df.area, df.price)
# plt.xlabel("Area"); plt.ylabel("Price")
# plt.show()

reg = linear_model.LinearRegression()
reg.fit(df[['area']], df.price)

print(reg.predict([[3000]]))

# print(prediction)


