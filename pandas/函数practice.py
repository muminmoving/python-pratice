import pandas as pd
data = pd.read_table("C:/Users/moving/Desktop/joyful-pandas-master/data/learn_pandas.csv",sep=",")
df = data[['Height', 'Weight']]
print(df.mean().head())
print(df.quantile(0.75))
print(data['School'].nunique())
print(data['School'].value_counts())
# drop_duplicateds后匹配columns记得加中括号
print(data[['Gender', 'Transfer', 'Name']].drop_duplicates(['Gender', 'Transfer'], keep="first"))