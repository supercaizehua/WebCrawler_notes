import random, time, multiprocessing


class MyProcess(multiprocessing.Process):

    def __init__(self, name, func):
        super().__init__()
        self.name = name
        self.func = func

    def run(self):
        self.func(self.name)


def worker(name):
    print(f'started worker {name}')
    worker_time = random.choice(range(1, 5))
    time.sleep(worker_time)
    print(f'{name} worker finished in {worker_time} seconds')


if __name__ == '__main__':
    processes = []
    for i in range(5):
        process = MyProcess(name=f'computer_{i}', func=worker)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
