'''
1、新建2个线程
2、定义一个线程执行函数，参数有name和delay
3、设置2个线程传递的参数分别为(php,2) (python,4)
4、实现线程在后台交替打印信息
'''
from threading import Thread
import time

def test(name,delay):
    for i in range(10):
        time.sleep(delay)
        print('%s:时间--%s'%(name,time.ctime(time.time())))
if __name__ == '__main__':
    t1 = Thread(target=test,args=('php',1),name='线程1')
    t2 = Thread(target=test,args=('python',1),name='线程2')
    t1.start()
    print(t1.name)
    t2.start()
    print(t2.name)


