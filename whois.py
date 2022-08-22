"""
爬取whois信息
https://www.whois.com/whois/
"""

import requests
import re
import os
website = input("请输入域名：")
url = 'https://www.whois.com/whois/%s'%website
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"
}
res = requests.get(url=url,headers=header)
# print(res.text)
html_str = res.text

# 解析数据  正则表达式
# class="df-label">(.*?)<.*?class="df-value">(.*?)</div>
pattern = re.compile('class="df-label">(.*?)<.*?class="df-value">(.*?)</div>', re.S)
result = pattern.findall(html_str)
# print(result)

# 创建目录
path = 'whois/'
if not os.path.exists(path):
    os.mkdir(path)

# for item in result:
#     print(item[0])
#     print(item[1])
#     print("\n")
with open(path+website+'.'+'txt', 'w') as fh:
    for item in result:
        # fh.write(item[0])
        # fh.write(item[1])
        # fh.write("\n")
        fh.write("%s%s\n"%(item[0],item[1]))
    print("保存完成...")


# 正则表达式
# class="df-label">Domain:</div><div class="df-value">baidu.com</div>
# class="df-label">(.*?)<.*?class="df-value">(.*?)</div>