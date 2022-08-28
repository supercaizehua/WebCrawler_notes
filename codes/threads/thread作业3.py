# 测试是否可以在单个子线程中再通过ThreadPoolExecutor创建线程池

import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

def longtime(*args):

    with ThreadPoolExecutor(max_workers=5) as executor:
        for arg in args:
            task = executor.submit(time.sleep, arg)


        print('finish')


t = threading.Thread(target=longtime, args = [10, 5, 3])

t.start()
t.join()

print('done')
