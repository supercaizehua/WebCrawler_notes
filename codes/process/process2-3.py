from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print(f'Put {value} to queue...')
        q.put(value)
        time.sleep(random.randint(1, 3))


def read(q):
    print(f'Process to read: {os.getpid()}')
    while True:
        value = q.get(True)
        print(f'Get {value} from queue.')


if __name__ == '__main__':
    # 父进程创建Queue, 并传递给各个子进程
    q = Queue()
    process_write = Process(target=write, args=[q])
    process_read = Process(target=read, args=[q])

    # 启动子进程 process_write, 写入:
    process_write.start()

    # 启动子进程 process_read, 读取:
    process_read.start()

    process_write.join()
    process_read.join()

    process_read.kill()