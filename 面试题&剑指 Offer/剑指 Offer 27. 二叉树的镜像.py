# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def mirrorTree(self, root):
        """
        https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return root
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return root
        # def dfs(node):
        #     if not node: return
        #
        #     dfs(node.left)
        #     dfs(node.right)
        #
        #     node.left, node.right = node.right, node.left
        #
        # dfs(root)
        # return root
