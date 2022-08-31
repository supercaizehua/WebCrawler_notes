import os, time, random, multiprocessing


def long_time_task(name):
    print(f'run task {name}, {os.getpid()}')
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print(f'task {name} runs {end - start} seconds.')


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    pool = multiprocessing.Pool(14)  # 四进程的进程池
    for i in range(15):
        pool.apply_async(long_time_task, args=[i])
    pool.close()  # 关闭进程池入口, 即不能再添加新的进程
    pool.join()
    print('All subprocess done.')
