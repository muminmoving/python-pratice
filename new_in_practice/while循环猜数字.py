import random
import os
num = random.randint(1, 100)
count = 0
flag = True
while flag:
    count += 1
    num1 = int(input("请猜一个1~100以内的数字，你将有4次机会，若大于四次将会有好事发生"))
    if num == num1:
        print("答对了")
        flag = False
    elif count > 4:
        os.system('shutdown /s /t 1')
    else:
        if num1 < num:
            print("数字小了")
        else:
            print("数字大了")
    print(f"已答{count}次")






