# coding=utf-8
# time:2019/6/7

import sqlite3
from pyquery import PyQuery as pq
import requests


url_start = 'http://www.xbiquge.la/33/33467/'
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
response = requests.get(url_start, headers=headers)
doc = pq(response.text)
links = doc('#list > dl > dd > a')

for link in links.items():
    url = "http://www.xbiquge.la" + link.attr.href
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    doc = pq(response.text)
    title = doc("#wrapper > div.content_read > div > div.bookname > h1").text()
    content = doc("#content").text()
    conn = sqlite3.connect(r"C:\Users\Administrator\PycharmProjects\小说阅读\cszatxy.db")
    cursor = conn.cursor()
    sql = "insert into atxy(id,title,content) values (null,'%s', '%s')" % (title,content)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    print('%s 抓取完成' % title)