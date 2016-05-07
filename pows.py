# -*- coding:utf-8 -*-


"""
乘方的天真实现
"""


def pows_easy(a, n):
    temp = 1
    for i in xrange(0, n):
        temp = temp * a
    return temp


"""
乘方的分治递归实现
"""


def pows(a, n):
    if n == 1:
        return a
    if n == 2:
        return a * a
    if n % 2 == 1:
        return pows(a, (n - 1) / 2) * pows(a, (n - 1) / 2) * a
    if n % 2 == 0:
        return pows(a, n / 2) * pows(a, n / 2)


if __name__ == '__main__':
    print pows(12, 6)
    print pows_easy(12, 6)
