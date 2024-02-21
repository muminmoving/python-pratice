import requests
import url_managers
from bs4 import BeautifulSoup
import re

root_url = "http://www.crazyant.net"

headers = {
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"
}

url_managers = url_managers.Url_manager()
urls = url_managers.add_new_url(root_url)
# 爬取链接
j = open("C:/Users\moving\Desktop\新建 文本文档 (2).txt", "w", encoding="UTF-8")
while url_managers.has_new_url():
    curr_url = url_managers.get_new_url()
    r = requests.get(curr_url,timeout=3, headers=headers)
    if r.status_code != 200:
        continue
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.title.string
    links = soup.find_all("a")
    j.write("Sucess:%s\t%s\n" % (curr_url, title))
    j.flush()
#传入所有链接
    for link in links:
        i = link.get("href")
        if i is None:
            continue
        pattern = r'^http://www.crazyant.net/\d+.html$'
        if re.match(pattern, i):
            url_managers.add_new_url(i)
j.close()
