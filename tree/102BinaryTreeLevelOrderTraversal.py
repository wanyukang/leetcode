#coding: utf-8


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, level):
        if not root:
            return
        if len(self.result) < level + 1:
            self.result.append([])
        if root.left:
            self.dfs(root.left, level + 1)
        if root.right:
            self.dfs(root.right, level + 1)
        self.result[level].append(root.val)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.result = []
        self.dfs(root, 0)
        return self.result
