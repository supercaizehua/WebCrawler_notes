import time
import functools


'''
写一个可以计算函数运行时间的装饰器
'''


def runtime(func):
    # 打印程序运行时间

    @functools.wraps(func)   #保留func的__name__等属性
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        # res 是为了得到原函数运行的结果
        res = func(*args, **kwargs)

        _runtime = time.perf_counter() - start_time

        print(f'{func.__name__} function runtime: [{_runtime}]')

        return res

    return wrapper


@runtime
def sum_list():
    a = [1 for _ in range(100000)]
    return sum(a)





if __name__ == '__main__':
    sum_list()