import seaborn as sns
import pandas as pd

# Load the 'tips' dataset
df = sns.load_dataset("tips")

# Quick look at the data
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

selcted_columns = df[["total_bill","tip"]]
print(selcted_columns)

filtered_rows = df[(df["total_bill"]>5.0) & (df["size"]==5)]
print(filtered_rows)
#save to csv
df.to_csv("data_2.csv")
#save to excel
df.to_excel("data_2.xlsx", index=False, engine="openpyxl")