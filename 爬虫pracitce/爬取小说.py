from bs4 import BeautifulSoup
import requests

# 爬取小说章节的链接
root_url = "http://www.89wx.cc/70/70610/"
url = "http://www.89wx.cc"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"
}

resp = requests.get(root_url, headers=headers)
soup = BeautifulSoup(resp.text, "html.parser")
links = soup.find_all("dd")
links_1 = []
s = open("C:/Users\moving\Desktop/1.txt", "w", encoding="utf8")
for link in links:
    link = link.find("a")
    link1 = link["href"]
    link_1 = url + link1
    title = link.string
    i = [link_1, title]
    print(f"正在爬取{title}")
    e = requests.get(link_1, headers=headers)
    e.encoding = "gbk"  # 纠正编码设置
    h = BeautifulSoup(e.text, "html.parser")
    # 可能需要调整这段代码，以正确地找到章节内容
    words = h.find_all("div", id="content")
    s.write(f"{title}\n{words}\n")
s.close()



