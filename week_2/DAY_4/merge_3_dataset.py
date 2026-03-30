import pandas as pd

df1 =pd.DataFrame({
    "Name":["A","B","C"],
    "Age":[29,27,25]
})
df2 =pd.DataFrame({
    "Name":["A","B","C"],
    "hobbies":["Cricket","songs","dance"]
})
df3 =pd.DataFrame({
    "Name":["A","B","C"],
    "Place":["blr","hvr","mys"]  
})
merged=pd.merge(df1,df2,how="inner",on="Name")
merged=pd.merge(merged,df3,how="inner",on="Name")
print(merged)

print(merged.info())
print(merged.describe())

