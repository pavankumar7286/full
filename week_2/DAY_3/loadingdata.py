import pandas as pd

# Load data from a CSV file
df_csv = pd.read_csv(r"C:\Users\pavankumar\OneDrive\Desktop\Full-Stack Ai(UDEMY)\week_2\DAY_3\data.csv")

print(df_csv.head())   # Show first 5 rows


data = {
    "Name": ["dhanu", "pooja", "misha"],
    "Age": [25, 30, 35],
    "City": ["chennai", "Delhi", "pune"]
}

# Save to Excel
pd.DataFrame(data).to_excel("data.xlsx", sheet_name="Sheet1", index=False, engine="openpyxl")

# Load it back
df_xlsx = pd.read_excel("data.xlsx", sheet_name="Sheet1", engine="openpyxl")
print(df_xlsx)


# Create a DataFrame directly from a Python dictionary
data_dict = {
    "Name": ["Ravi", "Sneha", "Kiran"],
    "Age": [22, 28, 31],
    "City": ["kanpur", "Hyderabad", "thiruvannamalai"]
}

df_dict = pd.DataFrame(data_dict)
print(df_dict)
