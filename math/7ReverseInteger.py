#coding: utf-8


class Solution:
    def reverse(self, x):
        """
        def reverse(self, x: int) -> int:
        """
        num = 0
        while x != 0:
            if x > 0:
                num = num*10 + x%10
                x = x//10
            else:
                num = num*10 + x%-10
                # print(num)
                x = x//-10*-1
        if num < -2**31 or num > 2**31 - 1:
            return 0
        return num