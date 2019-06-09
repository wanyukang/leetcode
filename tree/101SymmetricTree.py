#coding: utf-8


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        def isSymmetric(self, root: TreeNode) -> bool:
        """
        if not root:
            return True
        left = root.left
        right = root.right
        return self.is_same(left, right)

    
    def is_same(self, t1, t2):
        if not t1 and not t2:
            return True
        if not t1 and t2 or t1 and not t2:
            return False
        return t1.val == t2.val and self.is_same(t1.right, t2.left) and self.is_same(t1.left, t2.right)