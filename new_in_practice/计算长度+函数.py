name = "nihao"
i = len("nihao")
print(f"{i}")

# 计算长度
count = 0
for j in name:
    count += 1
print(f"{count}")


# 函数定义
def say_hi():
    print("Hello,world!")
    return None
print(type(say_hi()))

say_hi()


def susp():
    print("欢迎来到医院！\n请出示您的健康码以及72小时核酸证明")


susp()


# 函数的参数
def add(x, y):
    result = x + y
    print(f"{x}+{y}={result}")


add(4, 5)

# 案例
def check(x):
    print("欢迎来到医院，\n请出示你的72小时核酸证明。\n并配合测量体温")
    if x <= 37.5:
        print(f"您的体温是{x}°，体温正常请进入")
    else:
        print(f"您的体温是{x}°，体温异常，需要隔离！！！")


check(37.6)

# 函数的返回值
def add(a,b):
    result = a + b
    return result

r = add(3,4)
print(r)



