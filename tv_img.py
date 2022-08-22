'''
爬取图片
url:https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2817285601.jpg
'''

import re
import requests
# 爬取数据
url = "https://img2.doubanio.com/view/photo/s_ratio_poster/public/p2817285601.jpg"

response = requests.get(url=url)
# print(response.content)
img_data = response.content

with open('123.jpg', 'wb') as fh:
    fh.write()



