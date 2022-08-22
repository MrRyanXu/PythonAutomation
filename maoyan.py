'''
爬取猫眼Top100电影信息
https://www.maoyan.com/board
'''
import requests
import re
import os

# 爬取数据
page = int(input("请输入页码："))
limit = (page-1) * 10
url = 'https://www.maoyan.com/board/4?timeStamp=1642766870558&channelId=40011&index=2&signKey=c73043360da752d114581f6913aa1942&sVersion=1&webdriver=false&offset=%d'%limit
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"
}

responce = requests.get(url=url, headers=header)

html_str = responce.text
# print(html_str)




# 解析数据
pattern = re.compile('class="name"><.*?title="(.*?)".*?class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>', re.S)
result = pattern.findall(html_str)
# print(result)

# path = 'maoyan/'
# if not os.path.exists(path):
#     os.mkdir(path)
# for item in result:
#     print(item)
#     print(item[1].strip())






# 正则表达式
# <div class="movie-item-info">
#         <p class="name"><a href="/films/1200486" title="我不是药神" data-act="boarditem-click" data-val="{movieId:1200486}">我不是药神</a></p>
#         <p class="star">
#                 主演：徐峥,周一围,王传君
#         </p>
# <p class="releasetime">上映时间：2018-07-05</p>    </div>
# class="name"><.*?title="(.*?)".*?class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>


# 存储数据
with open('maoyanTop100.txt', 'w', encoding='utf-8') as fh:
    for item in result:
        # print(item[1].strip())
        fh.write("电影：%s--%s--%s\n"%(item[0], item[1].strip(), item[2]))
    print("保存成功....")
