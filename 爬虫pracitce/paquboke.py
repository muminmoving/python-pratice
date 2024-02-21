import requests
from bs4 import BeautifulSoup
import url_managers
import re

root_url = "http://www.crazyant.net"

urls = url_managers.Url_manager()
urls.add_new_url(root_url)

fout = open("C:/Users/moving/Desktop/新建 文本文档.txt", "w", encoding="UTF-8")
while urls.has_new_url():
    curr_url = urls.get_new_url()
    r = requests.get(curr_url, timeout=3)
    if r.status_code != 200:
        print("error, status_code is not 200", curr_url)
        continue
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.title.string

    fout.write("%s\t%s\n" % (curr_url, title))
    fout.flush()
    print("Sucess：%s,%s,%d" % (curr_url, title, len(urls.new_url)))

    links = soup.find_all("a")
    for link in links:
        href = link.get("href")
        if href is None:
            continue
        pattern = r'^http://www.crazyant.net/\d+.html$'
        if re.match(pattern, href):
            urls.add_new_url(href)

fout.close()
