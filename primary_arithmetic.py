# -*- coding: utf-8 -*-

dic_a = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
dic = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def str_to_num(s):
    shu = 0
    le = len(s)
    for mm in xrange(le):
        shu += dic[dic_a[s[mm]]] * (10 ** (le - 1 - i))
    return shu


while True:
    try:
        (n,) = (int(i) for i in raw_input().split())
        count0 = [0] * 10
        nums = []
        for i in xrange(n):
            nums.append(raw_input())
            count0[dic_a[nums[i][0]]] = 1  # 不能作为0出现
        # x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        max_ = 0
        ans = [0] * 9
        for i in xrange(10):
            for j in xrange(10):
                for k in xrange(10):
                    for l in xrange(10):
                        for m in xrange(10):
                            for n in xrange(10):
                                for o in xrange(10):
                                    for p in xrange(10):
                                        for q in xrange(10):
                                            for r in xrange(10):
                                                if i != j and j != k and k != l and l != m and m != n and n != o and o != p and p != q and q != r:
                                                    dic[dic_a['A']] = i
                                                    dic[dic_a['B']] = j
                                                    dic[dic_a['C']] = k
                                                    dic[dic_a['D']] = l
                                                    dic[dic_a['E']] = m
                                                    dic[dic_a['F']] = n
                                                    dic[dic_a['G']] = o
                                                    dic[dic_a['H']] = p
                                                    dic[dic_a['I']] = q
                                                    dic[dic_a['J']] = r
                                                    for i in xrange(10):
                                                        if dic[i] == 0 and count0[i]:
                                                            continue
                                                    su = 0
                                                    for zz in nums:
                                                        su += str_to_num(zz)
                                                    if su > max_:
                                                        max_ = su
                                                        ans = [i, j, k, l, m, n, o, p, q, r]
        print(ans)
    except EOFError:
        break
