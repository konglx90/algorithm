# -*- coding: utf-8 -*-

while True:
    try:
        n = int(raw_input())
        l = []
        for i in xrange(n):
            (x, y) = (int(j) for j in raw_input().split())
            if x == 1:
                l.append(y)
                if len(l) <= 2:
                    print "No"
                    continue
                _max = max(l)
                _all = sum(l)
                if _all - _max <= _max:
                    print "No"
                else:
                    print "Yes"
            else:
                l.remove(y)
                if len(l) <= 2:
                    print "No"
                    continue
                _max = max(l)
                _all = sum(l)
                if _all - _max <= _max:
                    print "No"
                else:
                    print "Yes"
    except EOFError:
        break
