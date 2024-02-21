money = 5000000
name = input("请输入您的姓名")


def check_rest():
    print("…………余额查询…………")
    print(f"{name}您的剩余存款为{money}")


def reserve(count):
    print("…………存款…………")
    global money
    money += count
    print(f"存款成功，\n剩余{money}元")


def output(count):
    print("…………取款…………")
    global money
    money -= count
    print(f"取款成功，\n剩余{money}元")

def main():
    print("请输入你想要的服务")
    global name
    print(f"{name},你好，请选择操作")
    print("查询输入\t输入1")
    print("存款\t\t输入2")
    print("取款\t\t输入3")
    print("退出\t\t输入4")
    return input("请输入你的选择")


while True:
    keyboard_input = main()
    if keyboard_input == "1":
        check_rest()
        continue
    elif keyboard_input == "2":
        count = int(input("取出金额"))
        output(count)
        continue
    elif keyboard_input == "3":
        count = int(input("存入金额"))
        reserve(count)
        continue
    else:
        print("退出了")
        break

