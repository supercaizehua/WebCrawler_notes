import multiprocessing
import time


def func(name):
    time.sleep(5)
    print('test process:', name)



if __name__ == '__main__':
    pl = []
    for i in range(5):
        name = f'python_process_{i}'
        p = multiprocessing.Process(target=func, args=[name])
        p.start()
        pl.append(p)

    for p in pl:
        p.join()

    print('main process finish!')
