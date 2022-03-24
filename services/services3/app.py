import time

import redis
from flask import Flask
from flask import request

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


def get_sum(value):
    a = value.get('a', 0)
    b = value.get('b', 0)
    return int(a) + int(b)


@app.route('/get-sum', methods=['POST'])
def calculate_sum():
    values = request.form
    print(f"value : {values}")
    total = get_sum(values)
    return {'total': total}


# @app.route('/')
# def hello():
#     count = get_hit_count()
#     return 'Hello World! I have been seen {} times.\n'.format(count)
