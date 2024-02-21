import re

import requests
from bs4 import BeautifulSoup
import os
headers ={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"
}

root_url = "https://pic.netbian.com/4kmeinv"
url_1 = "https://pic.netbian.com"

# 爬取html数据
def crawl_html(url):
    resp = requests.get(url, headers=headers)
    resp.encoding = "gbk"
    # 解析html
    soup = BeautifulSoup(resp.text, "html.parser")
    imgs = soup.find_all("a")

    # 获得图片地址
    urls_1 = []
    for img in imgs:
        img = str(img)
        scr = img[9: 27]
        url1 = url_1 + scr
        if "html" not in url1:
            continue
        pattern = r"^https://pic.netbian.com/tupian/\d+.html$"
        if re.match(pattern, url1):
            urls_1.append(url1)
    a = []
    for h in urls_1:
        h1 = requests.get(h, headers=headers)
        h1.encoding = "gbk"
        soup1 = BeautifulSoup(h1.text, "html.parser")
        img1 = soup1.find_all("img")
        img2 = img1[0]
        e = img2["src"]
        src = url_1 + e
    # 封装图片
        filename = os.path.basename(src)

        with open(f"C:/Users/moving/Desktop/图片封装1/{filename}", "wb") as f:
            resp_img = requests.get(src)
            f.write(resp_img.content)

urls = []
urls.append(root_url)
for i in range(2, 70):
    url2 = f"https://pic.netbian.com/4kmeinv/index_{i}.html"
    urls.append(url2)
for j in urls:
    crawl_html(j)
    print(f"{j}爬取中")