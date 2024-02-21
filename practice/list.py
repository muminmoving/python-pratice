names = ["Bob", "Tom", "Mary"]
invite = "一块吃个饭吧"
for i in range(0, 3):
    int(i)
    j = names[i]
    print(f"{j},{invite}!")
print("Bob将无法出席，请再邀请一人")
names.remove("Bob")
names.insert(0, "Kitty")
for i in range(0, 3):
    int(i)
    j = names[i]
    print(f"{j},{invite}!")

del names[0:]
print(names)

# 3-8
district = ["nihao", "wugongshang", "tenwangge", "poyanghu"]

#district.sort(reverse=False)
b = sorted(district, reverse=True)
print(b)