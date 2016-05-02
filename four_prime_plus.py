# -*- coding: utf-8 -*-


def is_prime(num):
    """
    判断一个数是否是素数
    :param num:
    :return:
    >>> is_prime(16)
    False
    >>> is_prime(17)
    True
    >>> is_prime(2)
    True
    >>> is_prime(15)
    False
    """
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    return not [y for y in range(3, int(num ** 0.5) + 1, 2) if num % y == 0]


def four_prime_plus(num):
    """
    将一个大于8的整数转换为四个质数之和， 本质根据还未被完全证明的欧几里得定理本质上问题是转换为两个质数的问题
    因为2+3+zhi_shu_1+zhi_shu_2==奇数， 2+2+zhi_shu_1+zhi_shu_2==偶数
    :param num:
    :return:
    """
    if num <= 7:
        print "Impossible"
        return
    if num % 2 == 0:
        first, second = 2, 2
    else:
        first, second = 2, 3
    for i in xrange(num / 2 + 1):
        if is_prime(i):
            pass
        else:
            continue
        for j in range(num)[::-1]:
            if is_prime(j) and i + j == num - first - second:
                print("{} + {} + {} + {} = {}".format(first, second, i, j, num))
                return

    print "Impossible"


if __name__ == "__main__":
    four_prime_plus(24)
    four_prime_plus(36)
    four_prime_plus(17)
    # import doctest

    # doctest.testmod(verbose=True)
