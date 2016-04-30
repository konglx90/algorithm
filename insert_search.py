# -*- coding: utf-8 -*-

"""
插值查找， 二分查找的进阶版
2.2 插值查找
首先考虑一个新问题，为什么一定要是折半，而不是折四分之一或者折更多呢？
打个比方，在英文字典里面查“apple”，你下意识翻开字典是翻前面的书页还是后面的书页呢？如果再让你查“zoo”，你又怎么查？很显然，这里你绝对不会是从中间开始查起，而是有一定目的的往前或往后翻。
同样的，比如要在取值范围1 ~ 10000 之间 100 个元素从小到大均匀分布的数组中查找5， 我们自然会考虑从数组下标较小的开始查找。
经过以上分析，折半查找这种查找方式，还是有改进空间的，并不一定是折半的！
mid = （low+high）/ 2, 即 mid = low + 1/2 * (high - low);
改进为下面的计算机方案（不知道具体过程）：mid = low + (key - a[low]) / (a[high] - a[low]) * (high - low)，也就是将上述的比例参数1/2改进了，根据关键字在整个有序表中所处的位置，让mid值的变化更靠近关键字key，这样也就间接地减少了比较次数。

分析：从时间复杂度上来看，它也是o(n)，但是对于表长较大，而关键字分布又比较均匀的查找表来说，插值查找算法的平均性能比折半查找要好的多。反之，数组中如果分布非常不均匀，那么差值查找未必是很合适的选择。
"""


def insert_search(a_list, num):
    """
    :param a_list:
    :param num:
    :return:
    >>> insert_search([1, 2, 3, 4, 5, 6], 4)
    3
    >>> insert_search([1, 2, 3, 4, 5, 6], 15)
    -1
    """
    if len(a_list) == 1 and a_list[0] == num:
        return 0
    else:
        left = 0
        right = len(a_list) - 1

        if a_list[right] < num or a_list[left] > num:
            return -1

        mid = left + (right - left) * (num - a_list[left]) / (a_list[right] - a_list[left])

        while left < right:
            if a_list[mid] == num:
                return mid
            elif a_list[mid] < num:
                left = mid + 1
                mid = left + (left - right) * (num - a_list[left]) / (a_list[right] - a_list[left])
            else:
                right = mid - 1
                mid = left + (left - right) * (num - a_list[left]) / (a_list[right] - a_list[left])
        if left == right and a_list[left] == num:
            return left
        return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
