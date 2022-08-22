import requests
import re
import os
from optparse import OptionParser

# 爬取数据
parse = OptionParser("python %prog -d domain -p page \n Example:python %prog -d baidu.com -p 5")
# 添加选项
parse.add_option('-d', '--domain', dest='domain', type='string', help='请输入要爬取的域名', default='baidu.com')
parse.add_option('-p', '--page', dest='page', type='int', help='请输入要爬取的页数', default='5')
# 接收参数
option, args = parse.parse_args()
domain = option.domain  # 域名
page = option.page
limit = page * 10
all_domain = []

for i in range(1, limit, 10):
    url = "https://cn.bing.com/search?q=site:%s&first=%d"%(domain, i)
    # print(url)
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"
    }
    response = requests.get(url=url, headers=header)
    # print(response.text)
    html_str = response.text

    # 解析数据
    pattern = re.compile('class="b_attribution"><cite>(.*?)<', re.S)
    result = pattern.findall(html_str)
    # print(result)
    domain_set = []  # 集合

    for item in result:
        sub_domain = item.split('//')[-1] + domain
        domain_set.append(sub_domain)
    all_domain.extend(domain_set)
all_domain = set(all_domain)
# print(all_domain)


# 保存数据
# 创建目录
path = 'd:/domain/'
if not os.path.exists(path):
    os.mkdir(path)

with open(path + domain + '.txt', 'w') as fh:
    for d in all_domain:
        fh.write("%s\n"%d)
print('文件已保存在%s'%(path + domain + '.txt'))