def insert_sort(a_list):
    """
    #>>> insert_sort([1, 12, 2, 4, 6, 15, 7])
    #[1, 2, 4, 6, 7, 12, 15]
    """
    if len(a_list) <= 1:
        return a_list
    for i in range(1, len(a_list)):
        key = a_list[i]
        # TODO
    return a_list


def half_search(a_list, num):
    """
    >>> half_search([1,2,3,5,45,123], 3)
    2
    >>> half_search([1,2,5,41,61], 61)
    4
    >>> half_search([1, 2, 5, 41, 61], 4)
    2
    >>> half_search([1, 2, 5, 41, 61], 42)
    4
    >>> half_search([1, 2, 5, 42, 61], 42)
    3
    """
    left = 0
    right = len(a_list) - 1
    mid = (left + right) / 2

    while a_list[mid] != num and right - left > 1:
        if a_list[mid] > num:
            right = mid - 1
            if (a_list[right] < num):
                return right + 1
        else:
            left = mid + 1
            if (a_list[left] > num):
                return left
        mid = (left + right) / 2
    if right - left == 1:
        if a_list[left] == num:
            return left
        if a_list[right] == num:
            return right
        else:
            return left + 1
    return mid


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    print insert_sort([1, 22, 4, 12, 16])
