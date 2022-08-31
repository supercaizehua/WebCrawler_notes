import os, time, random
from multiprocessing import Lock, Process


def f(lock, i):
    # try:
    #     lock.acquire()
    #     print(f'{i}:{os.getpid()} is running')
    #     time.sleep(random.randint(1, 3))
    #     print(f'{i}:{os.getpid()} is done!')
    # finally:
    #     lock.release()

    with lock:
        print(f'{i}:{os.getpid()} is running')
        time.sleep(random.randint(1, 3))
        print(f'{i}:{os.getpid()} is done!')

if __name__ == '__main__':
    lock = Lock()
    for num in range(10):
        Process(target=f, args=(lock, num)).start()
