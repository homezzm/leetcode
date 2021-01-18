# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)
            return max(left, right) + 1

        return dfs(root)
