# -*- coding: utf-8 -*-
import time
from functools import wraps


def timethis(func):
    """
    Decorator that reports the execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


def print_hello(func):
    def warp(*args, **kwargs):
        print("hello")
        return func(*args, **kwargs)
    return warp


@print_hello
@timethis
def countdown(n):
    while n > 0:
        n -= 1


countdown(100000)
