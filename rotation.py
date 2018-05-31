# -*- coding:utf-8 -*-
def rotation(step, a_list):
    """
    TestCase for rotation
    >>> rotation(1, [1,2,3,4,5])
    [5, 1, 2, 3, 4]
    >>> rotation(2, [1,2,3,4,5])
    [4, 5, 1, 2, 3]
    >>> rotation(7, [1,2,3,4,5])
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
