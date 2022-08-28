import time, random
from concurrent.futures import ThreadPoolExecutor, as_completed

def spider(url):
    '''爬虫方法'''
    time.sleep(random.randint(1,5))
    print(f'crawler task {url} finished')
    return url


#创建一个最大容量为5的线程池
with ThreadPoolExecutor(max_workers=5) as executor:
    urls = ['https://abc.com', 'https://efg.com', 'https://sdf.com', 'https://sdfs.com', 'https://abc.com', 'https://efg.com',  'https://hij.com',  'https://klm.com',  'https://nop.com',  'https://rsz.com']
    all_task = []
    for url in urls:
        #将任务提交到线程池中执行
        task = executor.submit(spider, url)

        #记录任务列表
        all_task.append(task)

    #阻塞, 获得任务完成后的返回值
    for future in as_completed(all_task):
        result = future.result()
        print(f'result: {result}')

    print('main finish')