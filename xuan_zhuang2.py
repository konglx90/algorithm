# -*- coding:utf-8 -*-
def xuan_zhuang(step, a_list):
    """
    TestCase for xuan_zhuang
    >>> xuan_zhuang(1, [1,2,3,4,5])
    [5, 1, 2, 3, 4]
    >>> xuan_zhuang(2, [1,2,3,4,5])
    [4, 5, 1, 2, 3]
    >>> xuan_zhuang(7, [1,2,3,4,5])
    [4, 5, 1, 2, 3]
    """
    step %= len(a_list)
    res(a_list, 0, len(a_list)-1)
    res(a_list, 0, step-1)
    res(a_list, step, len(a_list)-1)
    return a_list
def res(a_list, start, end):
    """
    辅助函数， 反向
    题目的要求是常数级空间复杂度， 要自己写res()
    """
    if len(a_list)<2 or start >= end:
        return
    middle = (start + end + 1) / 2
    for i in range(start, middle):
        temp = a_list[i]
        a_list[i] = a_list[end-(i-start)]
        a_list[end-(i-start)] = temp

def res2(a_list, start, end):
    """
    version_2 of res, 反转数组
    >>> res2([1,2,3,4,5,6,7,8,9,10], 0, 9)
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> res2([1,2], 0, 1)
    [2, 1]
    >>> res2([1], 0, 0)
    [1]
    """
    if len(a_list) < 2 or start >= end:
        return a_list
    while end-start > 0:
        a_list[start], a_list[end]= a_list[end], a_list[start]
        start += 1
        end -= 1
    return a_list

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
