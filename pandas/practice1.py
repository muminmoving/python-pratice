import pandas as pd
# 扩展窗口
data = [1, 3, 6, 10, 15]
s = pd.Series(data)
i = s[::-1].rolling(window=2).sum()
e = i.shift(-1)[::-1]

# 扩张窗口
f = s.expanding().mean()
f1 = s.cummax()
f2 = s.cumprod()
print(f2)


