import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def error(t):
    """没有返回值"""
    time.sleep(t)
    # 主动抛出异常
    raise Exception('This is Error')
    print(f'sleep {t}s')

with ThreadPoolExecutor(max_workers=5) as executor:
    all_task = []
    for i in range(5):
        task = executor.submit(error, 2)
        all_task.append(task)
    for future in as_completed(all_task):
        try:
            data = future.result()
        except Exception as e: # 异常处理
            print(f'work thread error: {e}')