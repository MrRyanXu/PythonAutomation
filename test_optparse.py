"""
命令行选项模块 optparse
"""

# 1 导入模块
from optparse import OptionParser

# 2 实例化对象
parse = OptionParser()

# 3 添加选项
parse.add_option('-d', '--domain', dest='domain', type='string', help='请输入要爆破的域名', default='baidu.com')
parse.add_option('-t', '--thread', dest='thread_num', type='int', help='请输入要爆破的线程数', default='10')

# 4 接收参数
option, args = parse.parse_args()
print(option)  # 字典
print(option.domain)
print(option.thread_num)
print(args)  # 列表
