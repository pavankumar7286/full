import pandas as pd

file_path = "data_2.xlsx"
xls = pd.ExcelFile(file_path, engine="openpyxl")
print(xls.sheet_names)

df = pd.read_excel(xls, sheet_name=xls.sheet_names[0])
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.describe())
print(df.isnull().sum())