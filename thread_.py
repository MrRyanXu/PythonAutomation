'''
多线程的使用
'''
# import test_main

# 多线程与多进程的区别

# 多线程 python多线程使用的是单核性能，线程都需要获取GIL锁 全局解析锁
# import threading  # 导入线程模块
# from threading import Thread  # 导入线程类
# # 定义线程函数
# def task():
#     while True:
#         pass
#
# if __name__ == "__main__":  # 判断当前程序是否为主程序
#     for i in range(4):
#         th = Thread(target=task)  # 定义线程对象
#         th.start()  # 开启线程




# 多进程 使用多核性能
# from multiprocessing import Process

# 定义线程函数
# def task():
#     while True:
#         pass
# if __name__ == '__main__':
#     for i in range(4):
#         p = Process(target=task)
#         p.start()
#

# 单线程搬砖任务
# import time
# def ban_zhuan(name):
#     print("%s开始搬砖..."%name)
#     time.sleep(2)
#     print("%s结束搬砖，一共搬了10000块砖"%name)
#
# if __name__ == '__main__':
#     start_time = time.time()  # 开始时间
#     for i in range(3):
#         ban_zhuan('Ryan')
#     end_time = time.time()  # 结束时间
#
#     print('一共花费了%s'%(end_time-start_time))


# 多线程搬砖任务
# import time
# from threading import Thread
# def ban_zhuan(name):
#     print("%s开始搬砖..."%name)
#     time.sleep(2)
#     print("%s结束搬砖，一共搬了10000块砖"%name)
#
# if __name__ == '__main__':
#     thread_list = []
#     start_time = time.time()  # 开始时间
#     for i in range(1,4):
#         th = Thread(target=ban_zhuan,args=('员工%s'%i,))
#         thread_list.append(th)
#     for t in thread_list:
#         t.start()
#     for t in thread_list:
#         t.join()  # 子线程同步
#     end_time = time.time()  # 结束时间
#
#     print('一共花费了%s'%(end_time-start_time))




# 通过线程池来控制线程数量
# from concurrent.futures import ThreadPoolExecutor
# import time
# def ban_zhuan(name):
#     print("%s开始搬砖..."%name)
#     time.sleep(2)
#     print("%s结束搬砖，一共搬了10000块砖"%name)
# with ThreadPoolExecutor(max_workers=10) as pool:
#     for i in range(1000):
#         pool.submit(ban_zhuan,i)


# 数据共享
# from threading import Thread
#
# def read_num(nums):
#     for i in nums:
#         print(i)
#
# def update_num(nums):
#     for i in nums[::-1]:
#         nums[i] = 0
#
# if __name__ == '__main__':
#     nums = list(range(1000))
#     read_th = Thread(target=read_num,args=(nums,))
#     update_th = Thread(target=update_num,args=(nums,))
#
#     read_th.start()
#     update_th.start()



# 互斥锁

from threading import Thread,Lock

def read_num(nums,lock):
    lock.acquire()  # 获取锁
    for i in nums:
        print(i)
    lock.release()  # 释放锁
def update_num(nums,lock):
    lock.acquire()  # 获取锁
    for i in nums[::-1]:
        nums[i] = 0
    # print(nums)
    lock.release()  # 释放锁

if __name__ == '__main__':
    nums = list(range(1000))
    lock = Lock()
    read_th = Thread(target=read_num,args=(nums,lock))
    update_th = Thread(target=update_num,args=(nums,lock))

    read_th.start()
    update_th.start()



