import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed, wait, ALL_COMPLETED

def spider(url):
    """爬虫方法"""
    time.sleep(random.randint(1, 5))
    print(f'crawl task {url} finished')
    return url

#  创建一个最大容纳数量为5的线程池
with ThreadPoolExecutor(max_workers=5) as executor:
    urls = ['https://abc.com', 'https://efg.com',  'https://hij.com',  'https://klm.com',  'https://nop.com',  'https://rsz.com']
    all_task = []
    for url in urls:
        task = executor.submit(spider, url)
        all_task.append(task)
    # 等待所有任务完成后再返回主线程
    wait(all_task, return_when=ALL_COMPLETED)
    print('----------')
    #下面其实已经是主线程的东西了
    for future in as_completed(all_task):
        result = future.result()
        print(f'result: {result}')
    print('main finish')