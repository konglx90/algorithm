# -*- coding: utf-8 -*-
def pa(n):
    """
    动态规划: 爬楼梯
    """
    if n == 1 or n==2:
        return n
    sum1 = 1
    sum2 = 1
    for i in range(1, n-1):
        temp = sum2
        sum2 = sum2 + sum1
        sum1 = temp
    print sum2

if __name__ == "__main__":
    pa(3)
    pa(4)
    pa(5)
    pa(6)
    pa(7)
    pa(120)
