import time
import requests
from urllib.parse import urlencode
headers = {
    "Content-Encoding": "gzip",
    "Content-Type": "application/json; charset=utf-8",
    "Date": "Sat, 11 Nov 2023 09:33:52 GMT",
    "Lb": "111.13.225.75",
    "Proc_node": "mapi-weibopro-node-bypass-56c67cd549-hgnzg",
    "Server": "SHANHAI-SERVER",
    "Ssl-Node": "mapi-10-185-8-140.yf.intra.weibo.cn",
    "Vary": "Accept-Encoding Origin",
    "X-Content-Type-Options": "nosniff",
    "X-Download-Options": "noopen",
    "X-Frame-Options": "SAMEORIGIN",
    "X-Log-Uid": "7486529029",
    "X-Readtime": "658",
    "X-Xss-Protection": "1; mode=block",
    "authority": "www.weibo.com",
    "method": "GET",
    "path": "/ajax/statuses/mymblog?uid=2348668214&page=1&feature=0",
    "scheme": "https",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Client-Version": "v2.44.22",
    "Cookie": "SUB=_2A25ISpmEDeRhGeFK41QU8ifMyTWIHXVrKZNMrDV8PUNbmtANLVHQkW9NQswO2Fj8XcdCrcnZjcFZxTUSSgV1998L; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5yZ1Y.-yX7s7sye1GLRU7U5JpX5KzhUgL.FoMX1hqfeo.7eo.2dJLoIpzLxKML1-zLB--LxKqLBoeLB-qt; ALF=1731206484; XSRF-TOKEN=-4HaJYimsa5ELDD6Vz8orr-P; WBPSESS=937pipFFJ2Yl2arJiBPPr2Ephe2wA88WR3WGxNscv8ohKwRLnG38Ru9TLsTnrEQ3t2ztBqrumFnx7DGLIdSCujJ9YMn8jalZqKea-6Jja8Z3PTtzsgL-tDwK9LY2csaf9EcPucZxXeHvQCdYRan1kQ==; _s_tentry=www.weibo.com; Apache=4478862087568.922.1699693020015; SINAGLOBAL=4478862087568.922.1699693020015; ULV=1699693020017:1:1:1:4478862087568.922.1699693020015:",
    "Referer": "https://www.weibo.com/u/2348668214",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Server-Version": "v2023.11.10.1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    "X-Requested-With": "XMLHttpRequest",
    "X-Xsrf-Token": "-4HaJYimsa5ELDD6Vz8orr-P"
}

root_url = 'https://www.weibo.com/ajax/statuses/mymblog?'


def get_pages(num):
    params = {
        'uid': 2348668214,
        'page': num,
        'feature': 0
    }
    url = root_url + urlencode(params)
    try:
        reponse = requests.get(url, headers=headers, params=params)
        if reponse.status_code == 200:
            return reponse.json()
        else:
            return None
    except ConnectionError:
        return None


def get_info(json):
    words = []
    if json:
        for i in range(0,21):
            try:
                items = json['data']['list'][i]
                word = items['text_raw']
            except IndexError:
                continue
            words.append(word)
        return words

if __name__ == "__main__":
    time.sleep(1)
    for num in range(1,100000):
        try:
            for i in get_info(get_pages(num)):
                with open("C:/Users/moving/Desktop/新建 文本文档 (3).txt", "a", encoding="utf8") as e:
                    if i == None:
                        continue
                    e.write(f"{i}\n\n")
                    e.flush()
        except TypeError:
            continue