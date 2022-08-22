"""
端口扫描工具
"""
# 1、指定一个ip和一个端口进行探测
# import socket
# ip = '127.0.0.1'
# port = 80
# try:
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.connect((ip, port))
# except:
#     print('[-] %s is colse' % port)
# else:
#     print('[-] %s is open' % port)

# 2、指定所有端口  range(1,65535)
# import socket
#
#
# def port_scan(ip, port):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.settimeout(0.1)  # 设置连接超时时间
#     try:
#         sock.connect((ip, port))
#     except:
#         print('[-] %s is colse' % port)
#     else:
#         print('[-] %s is open' % port)
#
#
# if __name__ == '__main__':
#     ip = '127.0.0.1'
#     for port in range(1, 65536):
#         port_scan(ip, port)

# 3、可以进行多个端口扫描 21,80,443,445, 2000-4000
# import socket
#
# def port_scan(ip, port):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.settimeout(0.1)  # 设置连接超时时间
#     try:
#         sock.connect((ip, port))
#     except:
#         # print('[---] %s is colse' % port)
#         pass
#     else:
#         print('[+++] %s is open' % port)
#
# if __name__ == '__main__':
#     ip = '127.0.0.1'
#     port_args = '21,80,443,445,2000-4000'
#     port_list = port_args.split(',')
#     # print(port_list)
#     all_port = []
#     for port in port_list:
#         # print(port)  # 字符串
#         if '-' not in port:
#             all_port.append(int(port))
#         else:
#             # print(port)
#             range_port = port.split('-')
#             # start = int(range_port[0])
#             # end = int(range_port[1])
#             port_range = list(range(int(range_port[0]), int(range_port[1])+1))
#             all_port.extend(port_range)
#     # print(all_port)
#
#     for port in all_port:
#         port_scan(ip, port)
#     print('====================扫描完成========================')

# 4、使用多线程进行扫描，并且用户可以控制线程数量
# import socket
# from concurrent.futures import ThreadPoolExecutor
# def port_scan(ip, port):
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.settimeout(0.1)  # 设置连接超时时间
#     try:
#         sock.connect((ip, port))
#     except:
#         pass
#     else:
#         print('[+++] %s is open' % port)
#
# if __name__ == '__main__':
#     thread_num = int(input("请输入扫描的线程数："))
#     ip = '127.0.0.1'
#     port_args = '21,80,443,445,2000-4000'
#     port_list = port_args.split(',')
#     all_port = []
#     for port in port_list:
#         # print(port)  # 字符串
#         if '-' not in port:
#             all_port.append(int(port))
#         else:
#             range_port = port.split('-')
#             port_range = list(range(int(range_port[0]), int(range_port[1])+1))
#             all_port.extend(port_range)
#     with ThreadPoolExecutor(max_workers=thread_num) as pool:
#         for port in all_port:
#             # port_scan(ip, port)
#             pool.submit(port_scan, ip, port)
#     print('====================扫描完成========================')
import socket
from concurrent.futures import ThreadPoolExecutor
from optparse import OptionParser

def port_scan(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)  # 设置连接超时时间
    try:
        sock.connect((ip, port))
    except:
        pass
    else:
        print('[+++] %s is open' % port)

if __name__ == '__main__':
    parse = OptionParser("%prog -i ip -p port -t thread \n Example: %prog -i 127.0.0.1 -p 80 -t 10")
    # 添加选项
    parse.add_option('-i', '--ip', dest='ip_addr', type='string', help='请输入要扫描的ip', default='127.0.0.1')
    parse.add_option('-p', '--port', dest='port', type='string', help='请输入要扫描的端口', default='1-65536')
    parse.add_option('-t', '--thread', dest='thread_num', type='int', help='请输入要扫描的线程数', default='20')
    # 接收参数
    option, args = parse.parse_args()
    ip = option.ip_addr
    port_args = option.port
    thread_num = option.thread_num
    port_list = port_args.split(',')
    all_port = []
    print('========================开始扫描========================')
    for port in port_list:
        # print(port)  # 字符串
        if '-' not in port:
            all_port.append(int(port))
        else:
            range_port = port.split('-')
            port_range = list(range(int(range_port[0]), int(range_port[1])+1))
            all_port.extend(port_range)
    with ThreadPoolExecutor(max_workers=thread_num) as pool:
        for port in all_port:
            # port_scan(ip, port)
            pool.submit(port_scan, ip, port)
    print('========================扫描完成========================')