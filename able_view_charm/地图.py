from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()
data = [
    ("北京市", 399),
    ("江苏省", 299),
    ("上海市", 199),
    ("江西省", 99)
]
map.add("地图", data, "china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1~9人", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10~99人", "color": "#FFFF99"},
            {"min": 100, "max": 199, "label": "100~199人", "color": "#FF9966"},
            {"min": 200, "max": 400, "label": "200~400人", "color": "#ff6666"}
    ])
)

map.render()
