i = True
while i:
    a = input("请输入一个数字")
    b = input("请输入第二个数字，我将为您与第一个数字相加")
    try:
        print(int(a) + int(b))
    except ValueError:
        print("请您输入数字")
    else:
        print(a + b)
        i = False