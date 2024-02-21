import json
from pyecharts.charts import Map
from pyecharts.options import *
# 数据处理与引入
f = open("C:/Users/moving/Desktop/1、Python快速入门（8天零基础入门到精通）/资料/第1-12章资料/资料/可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()
data_dict = json.loads(data)
province_data_list = data_dict["areaTree"][0]["children"]
# 列表中取出元组
data_list = []
for province_data in province_data_list:
    province_data_name = province_data["name"]+"省"
    province_data_confirm = province_data["total"]["confirm"]
    data_list.append((province_data_name, province_data_confirm))
# 生成地图
map1 = Map()
map1.add("疫情确诊人数", data_list, "china")
map1.set_global_opts(
    title_opts=TitleOpts(title="全国疫情确诊地图"),
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
map1.render("全国疫情确诊人数分布图.html")
