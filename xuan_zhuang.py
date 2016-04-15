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
    l = len(a_list)
    # 解决循环旋转浪费时间的问题
    step %= l
    while step:
        temp = a_list[l-1]
        for i in range(1, l)[::-1]:
            a_list[i] = a_list[i-1]
        a_list[0] = temp
        step -= 1
    return a_list

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
