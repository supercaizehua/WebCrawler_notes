import functools
import time


def runtime(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        _runtime = time.perf_counter() - start

        func_name = func.__name__
        print(f'{func_name} runtime: [{_runtime}]')
        return res

    return wrapper


@runtime
def recursive_multi(n):
    if n == 1: return 1
    if n <= 0: return None
    res = n * recursive_multi(n - 1)
    print(res)
    return res


recursive_multi(10)
