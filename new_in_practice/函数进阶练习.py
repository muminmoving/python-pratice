# 逻辑形式的传入
def test_func(compute):
    result = compute(1, 2)
    print(result)


def compute(x, y):
    return x + y


test_func(compute)


# 数据的传入
def add(x, y):
    print(f"{x + y}")
    return x + y


add(1, 3)


# 匿名函数
def test_func(compute1):
    result = compute1(1, 2)
    print(f"{result}")

test_func(lambda x, y:x * y)