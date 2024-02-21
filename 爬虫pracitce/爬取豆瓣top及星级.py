from bs4 import BeautifulSoup
import requests
import pandas

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"
}
# 爬取html
htmls = []
for startnum in range(0, 250, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={startnum}", headers=headers)
    html = response.text
    htmls.append(html)

data = []
for html in htmls:
    soup = BeautifulSoup(html, "html.parser")
    datas = (
        soup.find("div", attrs={"class": "article"})
        .find("ol", class_="grid_view")
        .find_all("div", class_="item")
    )
    for i in datas:
        rank = i.find("em").string
        title = i.find("div", class_="info").find("span", class_="title").string
        stars = (
            i.find("div", class_="info")
            .find("div", class_="bd")
            .find("div", class_="star")
            .find_all("span")
        )
        ranting_star = stars[0]["class"][0]
        ranting_num = stars[1].string
        comments = stars[3].string
        data.append(
            {"rank": rank,
             "title": title,
             "ranting_star": ranting_star,
             "ranting_num": ranting_num,
             "comments": comments
             }
        )
df = pandas.DataFrame(data)
df.to_excel("豆瓣top250.xlsx")
