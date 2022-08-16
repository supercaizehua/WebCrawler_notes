import time
import functools


def runtime(level='info'):
    def inner_decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            res = func(*args, **kwargs)
            _runtime = time.perf_counter() - start_time

            name = func.__name__
            if level == 'debug':
                print(f'{name} function runtime: [{_runtime}]')
            return res

        return wrapper

    return inner_decorate


@runtime(level='info')
def snooze():
    time.sleep(3)


snooze()
