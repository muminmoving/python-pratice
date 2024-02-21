from pyecharts.charts import Bar, Timeline
from pyecharts.options import *

bar1 = Bar()
bar1.add_xaxis(["中国", "俄罗斯", "美国"])
bar1.add_yaxis("2021年GDP", [60, 40, 50], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "俄罗斯", "美国"])
bar2.add_yaxis("2022年GDP", [70, 50, 40], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "俄罗斯", "美国"])
bar3.add_yaxis("2023年GDP", [80, 40, 30], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()
# 加入时间线
timeline = Timeline()
timeline.add(bar1, "point1")
timeline.add(bar2, "point2")
timeline.add(bar3, "point3")
# 时间线设置
timeline.add_schema(
    play_interval=3000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
timeline.render("各年GDP数据.html")
