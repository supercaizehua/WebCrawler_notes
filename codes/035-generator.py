def gen_nums():
    print("start")
    yield 1
    yield 2
    yield 3
    print("end")
    return None  # 可写可不写, 效果一样


n = 0
for i in gen_nums():
    print(f'{n} loop: {i}')
    n += 1
