import time
import threading

class MyThread(threading.Thread):
    def __init__(self, func, args, tname=''):
        # 调用父类构造函数
        # super.__init__()
        # super().__init__()
        threading.Thread.__init__(self)    #这一个写法在这个例子里面和上一行作用一样
        self.tname = tname
        self.func = func
        self.args = args

    # 线程执行的具体逻辑
    def run(self):
        self.func(*self.args)

def longtime(n):
    time.sleep(n)

def main():
    # 实例化线程
    t = MyThread(longtime, (10,), longtime.__name__)
    t.start()
    t.join()

if __name__ == '__main__':
    main()