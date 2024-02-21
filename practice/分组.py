import time
import random
i = int(input('请输入你要的组数'))
n = int(input('请输入总人数'))
my_list = []
# 获得一组人数
a_list_num = n // i
rest = n % i
# 获得分组排号
for j in range(1, n+1):
    my_list.append(j)
random.shuffle(my_list)
my_list = list(my_list)
# 分组
for j in range(0, rest):
    print(f'均分在组外的人为{my_list.pop()}')
a = 0
for h in range(1, i+1):
    print(f"组{h}为{my_list[a : a_list_num]}")
    e = my_list[a : a_list_num]
    for i in my_list[a : a_list_num]:
        my_list.remove(i)
print('马哥，分组完毕了')
time.sleep(1000)