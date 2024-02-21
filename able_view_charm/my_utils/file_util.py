# 接收路径文件并读取
def print_file_info(file_name):
    i = None
    try:
        i = open(file_name, "r", encoding="UTF-8")
        j = i.read()
        print("文件全部内容如下：")
        print(j)
    except Exception as e:
        print(f"程序出现问题原因为{e}")
    finally:
        # 判断i是否为None
        if i:
            i.close()


# 追加数据到指定文件中
def append_to_file(file_name, data):
    i = open(file_name, "a", encoding="UTF-8")
    j = i.write(data)

append_to_file("C:/Users/moving/Desktop/备份数据1.txt", "123456")