#coding: utf-8


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        def strStr(self, haystack, needle):
        """
        if not needle:
            return 0
        _h = list(haystack)
        _n = list(needle)
        n = 0
        h = 0
        for h in range(len(_h) - len(_n) + 1):
            for n in range(len(_n)):
                if _h[h + n] != _n[n]:
                    break
                if n == len(_n) - 1:
                    return h
        return -1