#coding: utf-8


class Solution:
    def isValid(self, s):
        """
        def isValid(self, s: str) -> bool:
        """
        if not s:
            return True
        stack = []
        for item in s:
            temp = ''
            if not stack:
                stack.append(item)
                continue
            if item == ')':
                temp = '('
            elif item == ']':
                temp = '['
            elif item == '}':
                temp = '{'
                
            if temp == stack[-1:][0]:
                stack.pop()
            else:
                stack.append(item)

        if stack:
            return False
        else:
            return True

    
if __name__ == "__main__":
    solution = Solution()
    s = "()[]{}"
    print(solution.isValid(s))