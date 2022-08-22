'''
爬取豆瓣书籍的作者和标题
https://book.douban.com/latest?icn=index-latestbook-all
'''
import requests
import re
# 爬取数据
url = "https://book.douban.com/latest?icn=index-latestbook-all"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"
}
response = requests.get(url=url, headers=header)
# print(response.text)
html_str = response.text


# 解析数据
# class="fleft".*?>(.*?)<.*?class="subject-abstract color-gray">(.*?)/
pattern = re.compile('class="fleft".*?>(.*?)<.*?class="subject-abstract color-gray">(.*?)/', re.S)
result = pattern.findall(html_str)
print(result)

# 正则表达式
# <div class="media__body">
#     <h2 class="clearfix">
#         <a class="fleft" href="https://book.douban.com/subject/35680662/">故事便利店</a>
#     </h2>
#     <p class="subject-abstract color-gray">
#         骆以军 / 2021-12 / 理想国｜河南文艺出版社 / 68.00元 / 平装
#     </p>
# class="fleft".*?>(.*?)<.*?class="subject-abstract color-gray">(.*?)/


# 保存数据
with open('book.txt', 'w', encoding='utf-8') as fh:
    for item in result:
        # print(item[1].strip())
        fh.write("书名:%s\n作者:%s\n" % (item[0], item[1].strip()))