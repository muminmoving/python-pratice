i = open("C:/Users/moving/Desktop/hoking.txt", "r", encoding="UTF-8")
print(type(i))
# 读取文件
print(f"{i.read(11)}")
print(f"{i.readline()}")
'''print(f"{i.readlines()}"
无法与for循环同时使用
'''
# for循环读取数据
for line in i:
    print(f"{line}")
