# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def isSymmetric(self, root):
        """
        https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(l, r):
            if not l and not r: return True
            if not l or not r or l.val != r.val: return False
            return dfs(l.left, r.right) and dfs(l.right, r.left)

        return dfs(root.left, root.right) if root else True
