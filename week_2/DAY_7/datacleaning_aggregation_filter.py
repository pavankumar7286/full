import pandas as pd

url = "https://raw.githubusercontent.com/pavankumar7286/full/refs/heads/main/data_2.csv"
df = pd.read_csv(url)

print(df.info())
print(df.describe())

df["size"]=df["size"].fillna(df["size"].median())
df["tip"]=df["tip"].fillna(df["tip"].mode()[0])

df=df.drop_duplicates()

first_class=df[df["smoker"]=="first"]