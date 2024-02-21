# 列表
name_list = ["李四", "张三", "赵四"]
print("name_list")
print(type(name_list))
index = name_list.index("李四")
print(f"{index}")
# 下标
my_name_list = [["李四", "张三", "赵四"], [666, 1.31, "你好"]]
print("name_list")
print(type(my_name_list))
print(my_name_list[-1][2])
# 修改下标的值
name_list.insert(2, '狂徒')
print(f"{name_list}")
# 练习
list1 = [21, 25, 21, 23, 22, 20, 31]

print(f"{list1}")
list1.extend([29, 33, 30])
print(f"{list1}")
num = list1.index(31)
print(f"{num}")

# 插入元素
list1.insert(0,"你好")

# 删除元素
del list1[1]
list1.pop()
print(list1)