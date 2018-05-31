# -*- coding:utf-8 -*-


"""
求解普通加法计算的进位次数
In: 123 456
Out: 0
In: 159 259
Out: 2
"""
while True:
    try:
        (x, y) = (int(i) for i in raw_input().split())
        if x == 0 and y == 0:
            break

        # 变成等长的列表
        x = (len(str(y)) - len(str(x))) * '0' + str(x) if len(str(x)) < len(str(y)) else str(x)
        y = (len(str(x)) - len(str(y))) * '0' + str(y) if len(str(y)) < len(str(x)) else str(y)
        x = [int(i) for i in str(x)]
        y = [int(i) for i in str(y)]

        l = len(x)
        count_jin = 0
        for i in range(l)[::-1]:
            if i == 0:
                if (x[i] + y[i]) >= 10:
                    count_jin += 1
            else:
                if (x[i] + y[i]) >= 10:
                    x[i - 1] += 1
                    count_jin += 1
        print count_jin
    except EOFError:
        break
