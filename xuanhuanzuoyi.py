# -*- coding: utf-8 -*-

while True:
    try:
        (n, K) = (int(j) for j in raw_input().split())
        list_of_str = []
        for i in xrange(n):
            list_of_str.append(raw_input())
        # while
    except EOFError:
        break
