# -*- coding: utf-8 -*-
# 16-04-14-T-01
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
    """
    for i in range(len(a_list))[:-1]:
        for j in range(i+1, len(a_list)):
            if a_list[i] + a_list[j] == value:
                return True
    return False
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
