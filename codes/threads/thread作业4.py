import time, threading
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, as_completed


def longtime(s):
    print(f'sleep {s}')
    time.sleep(s)
    print(f'{s} done')


def task_(s):
    t = threading.Thread(target=longtime, args=(s,))
    print('单个子线程开始')
    t.start()
    return t


with ThreadPoolExecutor(max_workers=3) as executor:
    all_task = []
    for i in [1, 3, 5, 7]:
        task = executor.submit(task_, i)
        all_task.append(task)

    # wait(all_task, return_when=ALL_COMPLETED)
    for future in as_completed(all_task):
        res = future.result()
        res.join()
        print('join')

    print('finish')
