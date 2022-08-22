"""
目录扫描工具
"""
# import requests
# from concurrent.futures import ThreadPoolExecutor
# def dir_scan(sub_dir,scan_url):
#     url = scan_url + sub_dir
#     print(url)
    # try:
    #     res = requests.get(url=url)
    # except:
    #     pass
    # else:
    #     if res.status_code == 200:
    #         print("%s 目录存在..." % url)

# if __name__ == '__main__':
#     scan_url = input("请输入爆破的域名：")  # 域名
#     thread_num = int(input("请输入爆破的线程数："))
#     print('----------------------开始扫描-----------------------')
#     with open('./DIR.txt','r') as fh:
#         sub_dir = fh.readline().strip()  # 子域名名称
#         with ThreadPoolExecutor(max_workers=thread_num) as pool:
#             while sub_dir:
#                 pool.submit(dir_scan, sub_dir, scan_url)
#                 sub_dir = fh.readline().strip()
#         print('----------------------扫描完成-----------------------')


#
import requests
from concurrent.futures import ThreadPoolExecutor
from optparse import OptionParser


def dir_scan(sub_dir,scan_url):
    url = scan_url + sub_dir
    try:
        res = requests.get(url=url)
    except:
        pass
    else:
        if res.status_code == 200:
            print("%s 目录存在..." % url)


if __name__ == '__main__':
    parse = OptionParser("python %prog -u url -t thread \n Example:python %prog -u http://baidu.com/ -t 10")
    # 添加选项
    parse.add_option('-u', '--url', dest='url', type='string', help='请输入要扫描的网址', default='http://baidu.com')
    parse.add_option('-t', '--thread', dest='thread_num', type='int', help='请输入要扫描的线程数', default='10')
    # 接收参数
    option, args = parse.parse_args()
    scan_url = option.url  # 域名
    thread_num = option.thread_num
    print('----------------------开始扫描-----------------------')
    with open('./DIR.txt','r') as fh:
        sub_dir = fh.readline().strip()
        with ThreadPoolExecutor(max_workers=thread_num) as pool:
            while sub_dir:
                pool.submit(dir_scan, sub_dir, scan_url)
                sub_dir = fh.readline().strip()
        print('----------------------扫描完成-----------------------')