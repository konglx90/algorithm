# -*- coding: utf-8 -*-

while True:
    try:
        (x, k) = (int(j) for j in raw_input().split())
        y = 1
        while True:
            if x+y == (x | y):
                k -= 1
            if k == 0:
                print y
                break
            y += 1
    except EOFError:
        break
