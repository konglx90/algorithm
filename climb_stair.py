# -*- coding: utf-8 -*-
def climb_stair(n):
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
    climb_stair(3)
    climb_stair(4)
    climb_stair(5)
    climb_stair(6)
    climb_stair(7)
    climb_stair(120)
