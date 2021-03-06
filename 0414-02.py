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
    # 使用内置的高效排序
    a_list = sorted(a_list)
    l = len(a_list)
    if a_list is None or l < 2:
        return False
    first_index = 0
    last_index = l - 1
    while first_index < last_index:
        if a_list[first_index] + a_list[last_index] == value:
            return True
        elif a_list[first_index] + a_list[last_index] < value:
            first_index += 1
        else:
            last_index += 1
    return False
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
