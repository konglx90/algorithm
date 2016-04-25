# -*- coding: utf-8 -*-
def max_sub(a_list):
    """
    最大下标距离, O(n**2)
    >>> max_sub([1,2,3,4,5,6])
    (0, 5)
    >>> max_sub([1,2,3,4,5,6,0])
    (0, 5)
    >>> max_sub([15, 48, 1, 1, 1, 24, 2, 12, 14, 1, 47, 1])
    (0, 10)
    """
    temp = 0
    i_index = 0
    j_index = 0
    l = len(a_list)
    for i in range(l-1):
        for j in range(i+1, l):
            if a_list[j] > a_list[i]:
                if j-i>temp:
                    temp = j-i
                    i_index = i
                    j_index = j
    return i_index, j_index

def max_sub2(a_list):
    """
    1的改进版
    """
    pass
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
