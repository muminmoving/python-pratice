import pandas as pd
import pyecharts
path = "C:/Users/moving/Desktop/joyful-pandas-master/data/my_table.txt"
data = pd.read_csv(path,sep="\t", usecols=["col3"])
print(data)
