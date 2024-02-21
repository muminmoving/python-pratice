# 反转字符串
def str_reverse(s):
    return s[::-1]

# 对字符串切片
def suster(s, x, y):
    """

    :param s:输入字符串
    :param x: 切片开端
    :param y: 切片结尾
    :return: 返回切片
    """
    s1= s[0: x:]
    s2 = s[x: y:]
    s3 = s[y::]
    print(f"{s1},{s2},{s3}")


if __name__ == '__main__':
    str_reverse("nihao")
    suster("nihaoa", 1, 3)