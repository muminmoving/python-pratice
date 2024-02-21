import json
data = [{"name": "王老五", "age": 16}, {"name": "王老六", "age": 30}, {"name": "王老七"," age": 20}]
json_str = json.dumps(data, ensure_ascii=False) # ensure_ascii = False 取消用ascii码转化，直接输出原内容
print(type(json_str))
print(json_str)

s = '[{"name": "王老五", "age": 16}, {"name": "王老六", "age": 30}, {"name": "王老七"," age": 20}]'
json_str1 = json.loads(s)
print(type(json_str1))