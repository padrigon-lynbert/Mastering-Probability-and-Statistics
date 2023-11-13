import pandas as pd

df = pd.read_csv("DataCSV\\pandas\\nyc_weather.csv")

# print(df)
# print(df['Temperature'].max())

#Days Rained
print(f" Data collected: Days Rained\n{df['EST'] [df['Events']=='Rain']}\n")

# average windspeed
df.fillna(0, inplace=True) #fill NaN (Cell with no data (NaN or Not a Number) with 0)
print(f" Data collected: Average Wind Speed\n{[df['WindSpeedMPH'].mean()]}")
