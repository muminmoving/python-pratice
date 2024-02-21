# 7-4 一
i = True
while i:
    material = input("请输入你想在比萨中加入的配料,如要结束请输入quit")
    if material == "quit":
        i = False
    else:
        print(f"将为你加入{material}")
# 二
while True:
    material = input("请输入你想在比萨中加入的配料,如要结束请输入quit")
    if material == "quit":
        break
    else:
        print(f"将为你加入{material}")

# 7-8
sandwich_orders = ["sandwich1", "sandwich2", "sandwich3", "sandwich4", "pastrami", "pastrami", "pastrami"]
finished_sandwiches = []
print("pastrami已经销售完毕")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
while sandwich_orders:
    print("I made your tuna sandwich")
    finished_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(finished_sandwich)
print(finished_sandwiches)
