import json
from pyecharts.charts import Map
from pyecharts.options import *

i = open("C:/Users/moving/Desktop/1、Python快速入门（8天零基础入门到精通）/资料/第1-12章资料/资料/可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = i.read()
i.close()
data_dict = json.loads(data)
data_list1 = data_dict["areaTree"][0]["children"][3]["children"]
data_list = []
for data1 in data_list1:
    data_name = data1["name"]+"市"
    data_confirm = data1["total"]["confirm"]
    data_list.append((data_name, data_confirm))
data_list.append(("济源市", 5))
map_henan = Map()
map_henan.add("河南省疫情人数", data_list, "河南")
map_henan.set_global_opts(
    title_opts=TitleOpts(title="河南省疫情图表"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1~99人", "color": "#CCFFFF"},
            {"min": 100, "max": 499, "label": "100~499人", "color": "#FFFF99"},
            {"min": 500, "max": 999, "label": "500~999人", "color": "#FF9966"},
            {"min": 1000, "max": 9999, "label": "1000~9999人", "color": "#ff6666"}
        ]
    )
)
map_henan.render("河南省疫情地图.html")
