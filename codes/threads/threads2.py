import time, threading


def longtime(s):
    time.sleep(s)


def main():
    # 实例化线程
    thread = threading.Thread(target=longtime, args=[10])
    print('Start', time.perf_counter())
    thread.start()
    thread.join()  # 将主线程挂起,等待子线程结束后才继续
    print('Done', time.perf_counter())


if __name__ == '__main__':
    main()
