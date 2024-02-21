# sort方法使用
"""
my_list = [["a", 33], ["b", 44], ["c", 55]]


def choose_sort_key(element):
    return element[1]


my_list.sort(key=choose_sort_key, reverse=True)
print(my_list)

my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)
"""
# 数据处理
from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *
j = open("C:/Users/moving/Desktop/1960-2019全球GDP数据.csv", "r", encoding="ANSI")
data_lines = j.readlines()
j.close()
data_lines.pop(0)
data_dict = {}
timeline = Timeline({"theme": ThemeType.LIGHT})
for data_line in data_lines:
    data_element = data_line.split(",")
    year = int(data_element[0])
    country = data_element[1]
    gdp = float(data_element[2])
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

i = sorted(data_dict.keys())
for year in i:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for e in year_data:
        x_data.append(e[0])
        y_data.append(e[1] / 100000000)

    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    timeline.add(bar, str(year))

timeline.add_schema(
    play_interval=3000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False,
)

timeline.render()
