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
    True
    """
    # 现将列表变为<value, index>字典
    if a_list is None or len(a_list) < 2:
        return False
    d = {}
    for i in range(len(a_list)):
        if d.has_key(a_list[i]):
            d[a_list[i]] = d[a_list[i]] + 1
        else:
            d[a_list[i]] = 1
    # 第二次遍历
    for i in a_list:
        if d.has_key(value-i):
        # 排除自己本身
            x = value == i*2
            if(not (x and d[i] == 1)):
                return True
    return False
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    #find(40, [14, 15, 16, 4, 6, 5])
