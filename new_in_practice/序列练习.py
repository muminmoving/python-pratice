my_str = "万过薪月，员序程马黑来，nohtyP学"
new_str = my_str[::-1][9:14]
print(f"{new_str}")

result = my_str.split("，")[1].replace("来", " ")[::-1]
print(f"{result}")
# 逗号记得区分
