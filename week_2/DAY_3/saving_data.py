import pandas as pd

data = pd.read_csv(r"C:\Users\pavankumar\OneDrive\Desktop\Full-Stack Ai(UDEMY)\week_2\DAY_3\data.csv")
# print(data.head())

data.to_excel("data.xlsx", sheet_name="Sheet1", index=False, engine="openpyxl")
data.to_csv("data_copy.csv", index=False)

#viewing data
print(data.head())
print(data.tail(2))  # Show last 2 rows
print(data.info())   # Get info about data types and non-null counts

print(data.describe())  # Get summary statistics for numeric columns
print(data[["Age","City","Name"]])  # Select specific columns

print(data[data["Age"] > 30])  # Filter rows where Age is greater than 30
print(data.iloc[0])  # Access first row by index
print(data.loc[:,"Name"])   # Access first row by label (same as iloc here