# -*- coding: utf-8 -*-
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        """采用两指针法
        """
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        left_index = 0
        right_index = len(s) - 1
        l = list(s)

        while left_index < right_index:
            if s[left_index] in vowels:
                if s[right_index] in vowels:
                    l[left_index], l[right_index] = l[right_index], l[left_index]
                    left_index += 1
                    right_index -= 1
                else:
                    right_index -= 1
            else:
                left_index += 1
        print("".join(l))


c = Solution()

c.reverseVowels("hello")
c.reverseVowels("leetcode")