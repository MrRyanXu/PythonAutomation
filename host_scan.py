"""
主机发现工具
"""

# 1、使用Scapy模块，指定一个IP进行探测
# from scapy.all import *
# from scapy.layers.inet import ICMP, IP
#
# dst_ip = '192.168.30.254'
# pkt = IP()/ICMP(seq=1000)/'hello'
# pkt[IP].dst = dst_ip
# # print(pkt.show())
#
# res = sr1(pkt, timeout=1, verbose=False)
# # print(res.show())
# if res:
#     print('[+++] %s 在线' % res[IP].src)


# 2、探测多个IP是否活跃  192.168.30.1-254
# from scapy.all import *
# from scapy.layers.inet import ICMP, IP
# import logging
# logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
#
# def host_scan(dst_ip):
#     pkt = IP()/ICMP(seq=1000)/'hello'
#     pkt[IP].dst = dst_ip
#     # print(pkt.show())
#     res = sr1(pkt, timeout=1, verbose=False)
#     # print(res.show())
#     if res:
#         print('[+++] %s 在线' % res[IP].src)
#     else:
#         print('[---] %s 不在线' % dst_ip)
# if __name__ == '__main__':
#     dst_ip = '192.168.30.1-254'
#     if '-' in dst_ip:
#         ip_tmp = dst_ip.split('-')
#         # print(ip_tmp)
#         end_ip = int(ip_tmp[-1])
#         # print(end_ip)
#         start_ip = int(ip_tmp[0].split('.')[-1])
#         # print(start_ip)
#
#         ip_prefix = ip_tmp[0][0:ip_tmp[0].rfind('.')+1]
#         # print(ip_prefix)  # 192.168.30.
#         for i in range(start_ip, end_ip+1):
#             d_ip = ip_prefix + str(i)
#             host_scan(d_ip)
#     else:
#         host_scan(dst_ip)

# 3、多线程扫描，加快速度
from concurrent.futures import ThreadPoolExecutor
from scapy.all import *
from scapy.layers.inet import ICMP, IP
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

def host_scan(dst_ip):
    pkt = IP()/ICMP(seq=1000)/'hello'
    pkt[IP].dst = dst_ip
    # print(pkt.show())
    res = sr1(pkt, timeout=3, verbose=False)
    # print(res.show())
    if res:
        print('[+++] %s 在线' % res[IP].src)
    else:
        # print('[---] %s 不在线' % dst_ip)
        pass
if __name__ == '__main__':
    thread_num = 50
    dst_ip = '192.168.30.1-254'
    if '-' in dst_ip:
        ip_tmp = dst_ip.split('-')
        # print(ip_tmp)
        end_ip = int(ip_tmp[-1])
        # print(end_ip)
        start_ip = int(ip_tmp[0].split('.')[-1])
        # print(start_ip)

        ip_prefix = ip_tmp[0][0:ip_tmp[0].rfind('.')+1]
        # print(ip_prefix)  # 192.168.30.
        print('======================开始扫描======================')
        with ThreadPoolExecutor(max_workers=thread_num) as pool:
            for i in range(start_ip, end_ip+1):
                d_ip = ip_prefix + str(i)
                pool.submit(host_scan, d_ip)
    else:
        host_scan(dst_ip)
    print('======================扫描结束======================')

# 4、使用命令行参数输入

