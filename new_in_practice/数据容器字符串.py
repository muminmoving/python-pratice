my_str = "mumin"
new_my_str = my_str.strip("m")
print({new_my_str})
# 遍历字符串
i = 0
while i < len(my_str):
    print(my_str[i])
    i += 1

for x in my_str:
    print(x)

# 案例练习
my_str1 = "itheima itcast boxuegu"
i = my_str1.count("it")
print(f"字符串itheima itcast boxuegu中有：{i}个字符")
# 替换字符
new_my_str1 = my_str1.replace(" ", "|")
print(f"字符串itheima itcast boxuegu,被替换空格后，结果：{new_my_str1}")

new_my_str1 = my_str1.strip()
print(f"字符串itheima itcast boxuegu,被替换空格后，结果：{new_my_str1}")
