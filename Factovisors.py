# -*- coding: utf-8 -*-
"""
阶乘和整除
"""


def gcd(a, b):
    return b if a == b or a % b == 0 else gcd(b, a % b)


while True:
    try:
        (n, m) = (int(i) for i in raw_input().split())
        _m = m
        if m < n:
            print("{0} divides {1}!".format(_m, n))
            continue
        for i in xrange(2, n + 1):
            m /= gcd(m, i)
        if m == 1:
            print("{0} divides {1}!".format(_m, n))
        else:
            print("{0} not divides {1}!".format(_m, n))
    except EOFError:
        break
