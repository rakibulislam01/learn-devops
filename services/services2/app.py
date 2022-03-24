import time

import redis
import requests
from flask import Flask

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


@app.route('/')
def hello():
    get_sum = requests.post('http://web3:5000/get-sum', data={"a": 1, "b": 2})
    total = get_sum.text
    return f"Total sum of the numbers: {total}"
