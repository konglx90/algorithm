# -*- coding: utf-8 -*-
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        ans = 1
        while ans < num:
            ans *= 4
            if ans == num:
                return True
        return False

    def isPowerOfFour2(self, num):
        """
        1. 转换成二进制只有首位是1是2的幂
        2. 满足1.的前提下， 从右往左数，1处在奇数位
        :param num:
        :return:
        """
        if self.isPowerOfTwo(num):
            s = bin(num)
            return len(s) % 2 != 0
        else:
            return False

    def isPowerOfTwo(self, num):
        return num > 0 and (not (num & (num - 1)))

c = Solution()

print c.isPowerOfFour(-2147483648)
print c.isPowerOfFour2(31)
print c.isPowerOfTwo(16)
