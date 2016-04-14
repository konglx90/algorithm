# -*- coding: utf-8 -*-
def find(value, a_list):
    """
    TestCase for find
    >>> find(26, [12,14])
    True
    >>> find(40, [14, 15, 16, 4, 6, 5])
    False
    >>> find(1, [1])
    False
    >>> find(1, [])
    False
    >>> find(4, [2, 3, 2])
    False
    """
    # 现将列表变为<value, index>字典
    if a_list is None or len(a_list) < 2:
        return False
    d = {}
    for i in range(len(a_list)):
        d[a_list[i]] = i
    # 第二次遍历
    for i in a_list:
        # 排除自己本身
        if(value-i in d and value != 2*i):
            return True
    return False
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
