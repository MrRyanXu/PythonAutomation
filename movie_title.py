'''
爬取豆瓣电影标题
https://movie.douban.com/chart
'''

import requests
import re

url = 'https://movie.douban.com/chart'
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"
}
res = requests.get(url=url,headers=header)
# print(res.status_code)
# print(res.text)
html_str = res.text

# 解析数据  正则表达式
# class="nbg".*?title="(.*?)"
pattern = re.compile('class="nbg".*?title="(.*?)"')
result = pattern.findall(html_str)
print(result)

# 保存数据
with open('movie_title.txt','w',encoding='utf-8') as fh:
    for index, item in enumerate(result):
        fh.write("%s:%s\n" % (index + 1, item))