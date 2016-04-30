# -*- coding: utf-8 -*-

"""
欧几里得问题
In: 17 17
Out: 0 1 17
In: 4 6
Out -1 1 2
"""


def gcd(a, b):
    return b if a == b or a % b == 0 else gcd(b, a % b)


while True:
    try:
        (A, B) = (int(i) for i in raw_input().split())
        D = gcd(A, B)

        X, Y = 0, 0

        while True:
            if X * A + Y * B == D:
                break
            elif X * A + Y * B > D:
                X -= 1
            elif X * A + Y * B < D:
                Y += 1
        print("{0} {1} {2}".format(X, Y, D))
    except EOFError:
        break
