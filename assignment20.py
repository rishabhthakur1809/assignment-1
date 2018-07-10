#Question1
import pandas as pd
import numpy as np
d={'name':pd.Series(['Prink','Singh']),
   'Age':pd.Series([29,30]),
   'Mobile number':pd.Series([998899,789086])}
df=pd.DataFrame(d)
print(df)
print(df.dtypes)
print(df.shape)
print(df.values)


#Question2
df=pd.read_csv('data.csv')
print(df)
print(df.head(5))
print(df.head(10))
print("mean",df.mean)
print("describe",df.describe())
print(df.tail(5))
print("LOCATION")
print(df['Location'])
print(df['Location'].describe)
print("MINTEMP")
print(df['MinTemp'].describe())
print("Count",df['MinTemp'].count())
print("Min",df['MinTemp'].min())
print("Var",df['MinTemp'].var())
print("Max",df['MinTemp'].max())
print("Mean",df['MinTemp'].mean())
print("Median",df['MinTemp'].median())
print("Mode",df['MinTemp'].mode())