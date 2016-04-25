#-*- coding: utf-8 -*-
def find_place_num(n, m):
    """

    """
    if n==1 or m==1:
        return 1
    else:
        return find_place_num(n-1, m) + find_place_num(n, m-1)


if __name__ == "__main__":
    print find_place_num(1, 1)
    print find_place_num(1, 2)
    print find_place_num(2, 1)
    print find_place_num(2, 2)
    print find_place_num(3, 4)
