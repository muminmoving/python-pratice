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
    imgs = soup.find_all("img")
    # 获得图片地址
    for img in imgs:
        src = img["src"]
        print(src)
        if "/uploads" not in src:
            continue
        url1 = url_1 + src
    # 封装图片
        filename = os.path.basename(src)

        with open(f"C:/Users/moving/Desktop/图片封装/{filename}", "wb") as f:
            resp_img = requests.get(url1)
            f.write(resp_img.content)

urls = []
for i in range(2, 70):
    url2 = f"https://pic.netbian.com/4kmeinv/index_{i}.html"
    urls.append(url2)
urls.append(root_url)

for j in urls:
    crawl_html(j)