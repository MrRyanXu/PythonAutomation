"""
爬取图片
http://616pic.com/png/
"""
import requests
import re
import os
from concurrent.futures import ThreadPoolExecutor

# 爬取数据
def get_data(page):
    url = 'http://616pic.com/png/%d.html'%page
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"
    }
    responce = requests.get(url=url, headers=header)
    html_str = responce.text
    # print(html_str)

    # 解析数据
    pattern = re.compile('data-original="(.*?)">.*?target="_blank" class=\'btitle\'>(.*?)</a>', re.S)
    result = pattern.findall(html_str)
    return result
    # print(result)

# 创建目录
path = 'PNG/'
if not os.path.exists(path):
    os.mkdir(path)

# 存储数据
def download_img(item):
    img_url = item[0]
    img_title = item[1]
    ext = img_url.split('.')[-1]  # 扩展名 jpg
    img_data = requests.get(img_url).content
    with open(path+img_title+'.'+ext, 'wb') as fh:
        # print(img_data)
        fh.write(img_data)
        print('%s下载完成...'%img_title)


if __name__ == '__main__':
    for i in range(1,51):
        result = get_data(i)
        with ThreadPoolExecutor(max_workers=20) as pool:
            for item in result:
                pool.submit(download_img, item)

# 正则表达式
# <img class="lazy" data-original="http://pic.616pic.com/ys_img/01/05/55/Qi7yJ5JShC.jpg">
# <a href="/sucai/14nikj49p.html" target="_blank" class='btitle'>2022时新年老虎节日元素</a>
# data-original="(.*?)">.*?target="_blank" class='btitle'>(.*?)</a>