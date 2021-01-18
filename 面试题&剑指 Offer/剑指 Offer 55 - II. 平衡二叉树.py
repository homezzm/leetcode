# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node):
            if not node: return 0

            left = dfs(node.left)
            if left == -1: return -1
            right = dfs(node.right)
            if right == -1: return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return dfs(root) != -1
