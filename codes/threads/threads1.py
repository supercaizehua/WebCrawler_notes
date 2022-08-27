import time

from concurrent.futures import ThreadPoolExecutor

from flask import Flask

executor = ThreadPoolExecutor(2)

app = Flask(__name__)


def longtime(s):
    time.sleep(s)


@app.route('/index')
def index():
    longtime(10)
    return 'hello sync Flask!'


@app.route('/index2')
def index2():
    executor.submit(longtime, 10)
    return 'hello async flask!'


if __name__ == '__main__':
    app.run()
