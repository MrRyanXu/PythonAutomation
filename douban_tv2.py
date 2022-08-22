'''
爬取豆瓣电视剧  图片和标题
https://movie.douban.com/j/search_subjects?type=tv&tag=热门&sort=recommend&page_limit=20&page_start=20
'''


# 使用线程来实现
import requests
import re
import os
from concurrent.futures import ThreadPoolExecutor
import time

# 爬取数据
def get_data():
    page = int(input("请输入页码:"))
    limit = page*20
    url = "https://movie.douban.com/j/search_subjects?type=tv&tag=热门&sort=recommend&page_limit=%d&page_start=0"%limit
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"
    }
    response = requests.get(url=url, headers=header)
    # print(response.text)
    json_data = response.text

    # 解析数据
    pattern = re.compile('"title":"(.*?)".*?"cover":"(.*?)"', re.S)
    result = pattern.findall(json_data)
    return result

# 创建目录
path = 'img/'
if not os.path.exists(path):
    os.mkdir(path)

def download_img(item):
    img_title = item[0]
    img_url = item[1].replace('\\', '')
    ext = img_url.split('.')[-1]  # 扩展名 jpg
    # print(ext)
    img_data = requests.get(img_url).content
    with open(path + img_title + '.' + ext, 'wb') as fh:
        fh.write(img_data)
        print("%s下载完成..." % img_title)

if __name__ == '__main__':
    start_time = time.time()
    result = get_data()
    with ThreadPoolExecutor(max_workers=10) as pool:
        for item in result:
            pool.submit(download_img, item)
    end_time = time.time()
    print('共花费时间：', end_time-start_time)

