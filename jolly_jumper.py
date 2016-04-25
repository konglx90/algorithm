# -*- coding: utf-8 -*-

"""
快乐的跳跃者
"""

while True:
    try:
        l = [int(i) for i in raw_input().split()]
        target_num = range(0, l[0])
        for i in range(1, l[0]):
            num = l[i + 1] - l[i]
            if num < l[0]:
                target_num[num] = 0
        not_jolly = False
        for i in target_num:
            if i != 0:
                not_jolly = True
        if not_jolly:
            print "Not Jolly"
        else:
            print "Jolly"
    except EOFError:
        break
