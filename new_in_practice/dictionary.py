# 字典的定义
my_dict = {"何青松": 90, "何宇鹏": 250,"hoking":36}
my_dict2 = {}
my_dict3 = dict()

# 不允许重复key,
i = my_dict["hoking"]
print(i)

# 字典的嵌套
stu_score_dict = {
    "hoking":{
    "语文": 100,
    "数学": 150,
    "英语": 399,
    }
}
j = stu_score_dict["hoking"]["语文"]
print(f"{j}")