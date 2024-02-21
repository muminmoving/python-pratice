
money = 10000
for x in range(1,21):
    import random
    num = random.randint(1, 10)
    if num >= 5:
        print(f"员工{x}，绩效分{num},发放工资1000元，账户余额剩余{money-1000}")
        money -= 1000
        if money <= 0:
            print("下月再领")
            break
    else:
        print(f"员工{x}绩点不足，跳过")
