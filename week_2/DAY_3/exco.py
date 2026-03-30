import pandas as pd

s = pd.Series([10,20,30], index = ['a','b','c'])
print(s)

data ={'Name':['pavan','kumar','virat'],'age':[25,30,35]}
df = pd.DataFrame(data)
print(df)