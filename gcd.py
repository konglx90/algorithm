# -*- coding: utf-8 -*-

"""
最大公约数
"""


def gcd(a, b):
    """
    需a>=b
    :param a:
    :param b:
    :return:
    """
    if a == b or a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def gcd_2(a, b):
    return b if a == b or a % b == 0 else gcd_2(b, a % b)


if __name__ == "__main__":
    print(gcd(34398, 2132))
    print(gcd_2(34398, 2132))
    print(gcd(9, 17))
