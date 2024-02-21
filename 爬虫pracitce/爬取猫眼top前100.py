import requests
from urllib.parse import urljoin
import time
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from lxml import etree
from pyquery import PyQuery as pq
# 爬取网站html
root_url = 'https://www.maoyan.com/board/4'
def get_onepage(url):
    try:
        headers = {
            'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
        }
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            print(f"{url}爬取成功")
            return resp.text
        else:
            return None
    except RequestException:
        print(f'{url}爬取失败')
        return None


# 爬取信息
def get_info_xpath(html):
    html = etree.HTML(html)
    result = html.xpath("//p[@class='name']/a/@href")
    for i in result:
        url = urljoin(root_url, i)
        print(url)
def get_pageinfo(html):
    soup = BeautifulSoup(html, 'html.parser')
    i = soup.find_all('p', class_='name')
    print(i)
def get_pageinfo_pyquery(html):
    doc = pq(html)
    pic_path = doc('.name a')
    pic_path = pic_path.attr('href')
    print(pic_path)

if __name__ == '__main__()':
    time.sleep(1)
    get_info_xpath(get_onepage(root_url))
