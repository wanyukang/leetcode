#coding: utf-8


class Solution:
    def gen(self, left_used, right_used, n, one):
        if left_used == n and right_used == n:
            self.list.append(one)
        if left_used < n:
            self.gen(left_used + 1, right_used, n, one + "(")
        if left_used > right_used and right_used < n:
            self.gen(left_used, right_used + 1, n, one + ")")
            
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1:
            return None
        self.list = []
        self.gen(0, 0, n, "")
        return self.list 