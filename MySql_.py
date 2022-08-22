'''
pymysql 使用
'''
import pymysql

conn = pymysql.connect(host='localhost',user='root',passwd='root')  # 连接数据库
cursor = conn.cursor()  # 创建游标

# 读写数据
sql = "show databases"
res = cursor.execute(sql)

# data = cursor.fetchone()  # 获取一条数据 返回的是元组
# data = cursor.fetchmany(10)  # 获取多条数据 返回的是二维元组
data = cursor.fetchall()  # 获取所有数据 返回的是元组
# print(data)
for item in data:
    print(item)

# 关闭
cursor.close()  # 关闭游标
conn.close()  # 关闭数据库连接

