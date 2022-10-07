from time import sleep, time
import logging
from functools import wraps


logging.basicConfig(filename='example.log',
                    encoding='utf-8',
                    level=logging.DEBUG)
my_logger = logging.getLogger('my_logger_1')


def benchmark(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        t1 = time()
        result = function(*args, **kwargs)
        t2 = time()
        duration = t2 - t1
        print(f"func run time {duration}")
        return result

    return wrapper


def logger_decor(function):
    @wraps(function)
    def log_wrapper(*args, **kwargs):
        my_logger.debug('Func running')
        result = function(*args, **kwargs)
        my_logger.debug('Func finished')
        return result

    return log_wrapper


@logger_decor
@benchmark
def slow_func(dur: int = 1, msg: str = 'default msg'):
    sleep(dur)
    print(msg)


slow_func(1, msg='hey')
