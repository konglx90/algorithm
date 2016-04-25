def insert_sort(a_list):
    """
    >>> insert_sort([1, 12, 2, 4, 6, 15, 7])
    [1, 2, 4, 6, 7, 12, 15]
    """
    if len(a_list) <= 1:
        return a_list
    for i in range(1, len(a_list)):
        key = a_list[i]
        j = i - 1
        while j > -1 and a_list[j] > key:
            a_list[j+1] = a_list[j]
            j -= 1
        a_list[j+1] = key
    return a_list

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print insert_sort([1, 22, 4, 12, 16])
