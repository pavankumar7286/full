import pandas as pd

url = "https://raw.githubusercontent.com/pavankumarsingh/Full-Stack-Ai-UDEMY/main/week_2/DAY_7/sales_data.csv"
df = pd.read_csv(url)

print(df.info())
print(df.describe())
