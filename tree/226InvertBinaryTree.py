#coding: utf-8


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """def invertTree(self, root: TreeNode) -> TreeNode:
        """
        if not root:
            return None
        temp_node = root.left
        root.left = root.right
        root.right = temp_node
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root