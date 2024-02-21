import pandas as pd
df = pd.read_csv("C:/Users/moving/Desktop/joyful-pandas-master/data/pokemon.csv")
total1_df = df[['HP', 'Attack', 'Defense','Sp. Atk', 'Sp. Def', 'Speed']]
total1 = total1_df.sum(axis=1)
# 判断列相等
'''i1 = []
i2 = []
for i in total1:
    i1.append(i)
for j in df['Total']:
    i2.append(j)
if i2 == i1:
    print("True")
else:
    print("False")'''

is_equal = df['Total'].equals(total1)
print(is_equal)
# 去重
print(df["Name"].nunique())
df1 = df.drop_duplicates(['Name'], keep='first')

print(df["Type 1"].nunique())
print(df['Type 2'].value_counts().head())
# b
df3 = df[['Type 1', 'Type 2']]
print(df3.drop_duplicates(['Type 1', 'Type 2'], keep=False))
df3 = df3.drop_duplicates(['Type 1', 'Type 2'])
print(df3.shape[0])

#c
L_full = [' '.join([i, j]) if i != j else i for j in df3['Type 1'].unique() for i in df3['Type 1'].unique()]
L_part = [' '.join([i, j]) if type(j) != float else i for i, j in zip(
    df3['Type 1'], df3['Type 2'])]
res = set(L_full).difference(set(L_part))
