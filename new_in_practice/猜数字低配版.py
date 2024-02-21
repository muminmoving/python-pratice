import random
num = random.randint(1,10)
num1 = int(input("请猜测一个0~10以内的数字"))
if num == num1:
    print("恭喜答对")
else:
    if num > num1:
        print("猜小了")
    else:
        print("猜大了")
    num1 = int(input("请再猜测一个0~10以内的数字"))
    if num == num1:
        print("恭喜答对")
    if num > num1:
        print("猜小了")
    else:
        print("猜大了")
    num1 = int(input("请再猜测一个0~10以内的数字"))
    if num == num1:
        print("恭喜答对")
        if num > num1:
            print("猜小了")
        else:
            print("猜大了")
    else:
        print("没机会了")


