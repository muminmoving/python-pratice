# 10-1
i = open("C:/Users\moving\Desktop\新建 文本文档 (2).txt", "r", encoding="UTF-8")
e = i.read()
print(e)
#j = i.readlines()
#print(j)
i.close()
# 10-3
with open("C:/Users\moving\Desktop\新建 文本文档 (2).txt", "a", encoding="UTF-8") as e:
    j = input("请输入您的用户名")
    e.write(j)
    # 10-4
    hello = "hello,user"
    while True:
        g = input("请输入您的用户名")
        print(f"\n{hello + g}")
        e.write(hello + g)
        f = input("你为什么喜欢编程")
        e.write(f"\n{f}")
