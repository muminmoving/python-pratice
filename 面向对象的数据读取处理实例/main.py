from file_define import *
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
text_filereader = Text_filereader("C:/Users/moving/Desktop/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年1月销售数据.txt")
json_filereader = Json_filereader("C:/Users/moving/Desktop/1、Python快速入门（8天零基础入门到精通）/资料/第13章资料/2011年2月销售数据JSON.txt")
data1: list[Record] = text_filereader.reader()
data2: list[Record] = json_filereader.reader()

data: list[Record] = data1 + data2
data_dict = {}
for i in data:
    if i.date in data_dict.keys():
        data_dict[i.date] += i.money
    else:
        data_dict[i.date] = i.money

bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))

bar.add_xaxis(list(data_dict.keys())),
bar.add_yaxis("销售额", list(data_dict.values()), label_opts=LabelOpts(is_show=False))

bar.set_global_opts(
    title_opts=TitleOpts(title="每日营销额图")
)
bar.render()

