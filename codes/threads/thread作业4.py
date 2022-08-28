import time, threading
from concurrent.futures import ThreadPoolExecutor


def longtime(s):
    print(f'sleep {s}')
    time.sleep(s)
    print(f'{s} done')


def task_(s):
    t = threading.Thread(target=longtime, args=(s,))
    print('单个子线程开始')
    t.start()


with ThreadPoolExecutor(max_workers=3) as executor:
    for i in [1, 3, 5, 7]:
        task = executor.submit(task_, i)

    print('finish')
