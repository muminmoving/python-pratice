# 5-3
alien_color = "red"
if alien_color == "green":
    print("你获得5分")
else:
    print("你获得10分")

# 5-5
alien_color = "yellow"
if alien_color == "green":
    print("你获得5分")
elif alien_color == "yellow":
    print("你获得10分")
else:
    print("你获得15分")

# 5-6
age = int(input("请输入你的年龄"))
if age < 2:
    print("你是婴儿")
elif age < 4:
    print("你是幼儿")
elif age < 13:
    print("你是儿童")
elif age < 20:
    print("你是青少年")
elif age < 65:
    print("你是成年人")
else:
    print("你是老年人")

# 5-8
users = [" a", "b", "c", "admin", "e"]
for i in users:
    if i == "admin":
        print("Hello admin,would you like to see a status report?")
    else:
        print(f"Hello {i},thank you for logging in again")

# 5-9
if users:
    del users[:]
else:
    print("We need to find some users!")
print(users)

# 5-11
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for j in num:
    if j == 1:
        print("1st")
    elif j == 2:
        print("2nd")
    elif j == 3:
        print("3rd")
    else:
        print(f"{j}th")
