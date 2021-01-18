# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        q, res = deque(), []
        q.append(root)
        while q:
            res.append([i.val for i in q])
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
