# 用while循环列出列表元素
my_list = [6, "nihao", "你的名字"]
index = 0
while index < len(my_list):
    element = my_list[index]
    print(f"{element}")
    index += 1

# 用for循环列出列表元素
my_list1 = [1, 2, 3, 4]
for i in my_list1:
    print(f"{i}")

# 练习案例
# while循环演示
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list3 = []
j = 0
while j < len(my_list2):
    if my_list2[j] % 2 == 0:
        my_list3.append(my_list2[j])
        print(f"{my_list3}")
    j += 1

# for循环演示
my_list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list3 = []
for j in my_list4:
    if j % 2 == 0:
        my_list3.append(j)
        print(f"{my_list3}")








