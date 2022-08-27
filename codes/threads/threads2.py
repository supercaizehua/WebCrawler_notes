import time, threading


def longtime(s):
    time.sleep(s)


def main():
    # 实例化线程
    thread = threading.Thread(target=longtime, args=[10])
    thread.start()
    thread.join()  #将主线程挂起,等待子线程结束后才继续
    print('111111111111')


if __name__ == '__main__':
    main()
