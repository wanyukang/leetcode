#coding: utf-8


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class DFSSolution:
    def dfs(self, root):
        if not root:
            return
        self.result.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)

    def traversalTrees(self, root):
        if not root:
            return []
        self.result = []
        self.dfs(root)
        return self.result

class BFSSolution:
    def traversalTrees(self, root):
        if not root:
            return []
        self.result = []
        q = []
        q.append(root)
        while len(q) > 0:
            node = q.pop(0)
            self.result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return self.result