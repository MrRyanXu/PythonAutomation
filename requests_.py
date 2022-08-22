'''
requests 库的使用
'''

import requests

response = requests.get('http://www.baidu.com')
print(response.status_code)
print(response.text)
print(response.content)  # 爬取流数据  使用的保存方式





