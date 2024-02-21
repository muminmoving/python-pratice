ir = open("C:/Users/moving/Desktop/备份数据.txt", "r", encoding="UTF-8")
iw = open("C:/Users/moving/Desktop/备份数据1.txt", "w", encoding="UTF-8")
for line in ir:
    line = line.strip()
# 生成列表再使用索引
    if line.split(",")[4] == "测试":
        continue
    iw.write(line)
    iw.write("\n")
iw.close()
ir.close()


