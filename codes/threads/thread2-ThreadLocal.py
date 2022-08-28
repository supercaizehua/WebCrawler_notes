import threading

local_value = threading.local()  # 全局ThreadLocal变量


def get_name():
    name = local_value.name  # 获取当前线程中的内容
    print(f'hello {name}')


def my_thread(name):
    local_value.name = name  # 改变当前线程中的变量
    get_name()


t1 = threading.Thread(target=my_thread, args=['oneone'], name='t1')
t2 = threading.Thread(target=my_thread, args=['twotwo'], name='t2')
t1.start()
t2.start()