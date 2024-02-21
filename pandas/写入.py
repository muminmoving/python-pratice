import pandas as pd

s = pd.Series(data=[1, 2, 3, 4],
              index=pd.Index(["a", "b", "c", "d"],name='user'),
              dtype='object',
              name='use')
data = [[1, 'a', 1.2], [2, 'b', 2.2], [3, 'c', 3.2]]
s1 = pd.DataFrame(data=data,
                  index = ['row_%d'%i for i in range(3)],
                  columns=(['col_0', 'col_1', 'col_2'])
)
print(s1.T)