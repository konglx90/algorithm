#  -*- coding: utf-8 -*-

# 斐波那契的四种实现与比较
# 用fib(100)来比较


def fib1(n):
    """递归法， 复杂度高"""
    if n==1 or n==2:
        return 1
    else:
        return fib1(n-1)+fib1(n-2)


def fib2(n):
    """迭代法， 复杂度一般"""
    if n==1 or n==2:
        return 1
    first = 1
    second = 1
    temp = 0
    for i in xrange(n-2):
        temp = first + second
        first, second = second, temp
    return temp


def fib3(n):
    """通项法， 复杂度极低， 但在计算机上有精度问题"""
    import math
    sqrt_5 = math.sqrt(5)
    return int(sqrt_5/5.0*(((1+sqrt_5)/2.0)**n-((1-sqrt_5)/2.0)**n))


def fib4(n):

    """矩阵乘法， 复杂度低， 无精度问题， Ok"""
    t = [[1, 1], [1, 0]]
    two(n, t)
    return t[0][0]

def two(n, t):
    """计算2维矩阵的辅助函数"""
    if n == 1:
        n = 2
    for i in range(n-2):
        t[0][0], t[0][1], t[1][0], t[1][1] = t[0][0]+t[0][1], t[0][0], t[1][0]+t[1][1], t[1][0]

if __name__ == '__main__':
    #print fib1(100)
    print fib2(10)
    print fib3(10)
    print fib4(10)
