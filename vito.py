# -*- coding: utf-8 -*-
import math

while True:
    try:
        (x,) = (int(i) for i in raw_input().split())
        for i in xrange(x):
            num = [int(i) for i in raw_input().split()]
            sort_num = sorted(num[1:])
            if num[0] % 2 != 0:
                middle = sort_num[num[0] / 2]
            else:
                middle = int((sort_num[num[0] / 2] + sort_num[num[0] / 2 - 1]) / 2)
            shortest = 0
            for j in sort_num:
                dis = middle - j
                shortest += math.fabs(dis)
            print int(shortest)
    except EOFError:
        break
