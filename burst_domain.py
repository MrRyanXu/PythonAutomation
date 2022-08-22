"""
子域名爆破工具
要求：通过暴力破解来获得子域名，类似子域名挖掘机的功能
1、指定域名进行爆破 ：toutiao.com
2、指定域名字典进行爆破 ：toutiao.com
3、使用多线程，加快爆破速度
4、输入任意域名，指定线程数量，进行爆破
5、使用命令行参数，执行脚本（完善的脚本）
"""
# import requests
#
# # 1、指定域名进行爆破 ：toutiao.com
# sub_name = 'www'  # 子域名名称
# domain = 'toutiao.com'  # 域名
# sub_domain = sub_name+ '.' + domain
# url = 'http://' + sub_domain
# res = requests.get(url=url)
#
# # print(url)
# # print(res.status_code)  # 状态码 200
# if res.status_code == 200:
#     print("%s 子域名存在..."%sub_domain)


# 2、指定域名字典进行爆破 ：toutiao.com
# import requests
# with open('./sub_name.txt','r') as fh:
#     sub_name = fh.readline().strip()  # 子域名名称
#     while sub_name:
#         domain = 'baidu.com'  # 域名
#         sub_domain = sub_name+ '.' + domain
#         # print(sub_domain)
#         url = 'http://' + sub_domain
#         try:
#             res = requests.get(url=url)
#         except:
#             # print("%s 子域名不存在..."%sub_domain)
#             pass
#         else:
#             if res.status_code == 200:
#                 print("%s 子域名存在..."%sub_domain)
#         finally:
#             sub_name = fh.readline().strip()


# 3、使用多线程，加快爆破速度
# import requests
# from concurrent.futures import ThreadPoolExecutor
# def burst_domain(sub_name,domain):
#     sub_domain = sub_name + '.' + domain
#     # print(sub_domain)
#     url = 'http://' + sub_domain
#     try:
#         res = requests.get(url=url)
#     except:
#         # print("%s 子域名不存在..."%sub_domain)
#         pass
#     else:
#         if res.status_code == 200:
#             print("%s 子域名存在..." % sub_domain)
#
# if __name__ == '__main__':
#     domain = 'baidu.com'  # 域名
#     with open('./sub_name.txt','r') as fh:
#         sub_name = fh.readline().strip()  # 子域名名称
#         with ThreadPoolExecutor(max_workers=10) as pool:
#             while sub_name:
#                 pool.submit(burst_domain, sub_name, domain)
#                 sub_name = fh.readline().strip()


# 4、输入任意域名，指定线程数量，进行爆破
# import requests
# from concurrent.futures import ThreadPoolExecutor
# def burst_domain(sub_name,domain):
#     sub_domain = sub_name + '.' + domain
#     # print(sub_domain)
#     url = 'http://' + sub_domain
#     try:
#         res = requests.get(url=url)
#     except:
#         # print("%s 子域名不存在..."%sub_domain)
#         pass
#     else:
#         if res.status_code == 200:
#             print("%s 子域名存在..." % sub_domain)
#
# if __name__ == '__main__':
#     domain = input("请输入爆破的域名：")  # 域名
#     thread_num = int(input("请输入爆破的线程数："))
#     with open('./sub_name.txt','r') as fh:
#         sub_name = fh.readline().strip()  # 子域名名称
#         with ThreadPoolExecutor(max_workers=thread_num) as pool:
#             while sub_name:
#                 pool.submit(burst_domain, sub_name, domain)
#                 sub_name = fh.readline().strip()


# 5、使用命令行参数，执行脚本（完善的脚本）
import requests
from concurrent.futures import ThreadPoolExecutor
from optparse import OptionParser


def burst_domain(sub_name,domain):
    sub_domain = sub_name + '.' + domain
    # print(sub_domain)
    url = 'http://' + sub_domain
    try:
        res = requests.get(url=url)
    except:
        # print("%s 子域名不存在..."%sub_domain)
        pass
    else:
        if res.status_code == 200:
            print("%s 子域名存在..." % sub_domain)


if __name__ == '__main__':
    parse = OptionParser("%prog -d domain -t thread \n Example: %prog -d baidu.com -t 10")
    # 添加选项
    parse.add_option('-d', '--domain', dest='domain', type='string', help='请输入要爆破的域名', default='baidu.com')
    parse.add_option('-t', '--thread', dest='thread_num', type='int', help='请输入要爆破的线程数', default='10')
    # 接收参数
    option, args = parse.parse_args()
    domain = option.domain  # 域名
    thread_num = option.thread_num
    print('----------------------开始爆破-----------------------')
    with open('./sub_name.txt','r') as fh:
        sub_name = fh.readline().strip()  # 子域名名称
        with ThreadPoolExecutor(max_workers=thread_num) as pool:
            while sub_name:
                pool.submit(burst_domain, sub_name, domain)
                sub_name = fh.readline().strip()
        print('----------------------爆破完成-----------------------')
