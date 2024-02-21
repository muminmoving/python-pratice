i = open("C:/Users/moving/Desktop/word.txt", "r", encoding="UTF-8")
j = i.read()
count = j.count('itheima')
print(f"{count}")
i.close()
# 一行一行读取数据
count = 0
i = open("C:/Users/moving/Desktop/word.txt", "r", encoding="UTF-8")
for line in i:
    line = line.strip()
    line = line.split()
    print(f"{line}")
    for word in line:
        if word == "itheima":
            count += 1
print(f"{count}")