#coding: utf-8


class Solution:
    def isPalindrome(self, s):
        """
        def isPalindrome(self, s: str) -> bool:
        """
        new = []
        for item in s.lower():
            if item.isalnum():
                new.append(item)
        l = 0
        r = len(new) - 1
        while l < r:
            if new[l] != new[r]:
                return False
            else:
                l += 1
                r -= 1
        return True