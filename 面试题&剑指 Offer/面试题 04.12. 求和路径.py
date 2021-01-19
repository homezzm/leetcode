# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        https://leetcode-cn.com/problems/paths-with-sum-lcci/
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root: return 0
        def dfs(node, sumVal):
            if not node: return 0
            res = 0
            if node.val == sumVal:
                res += 1
            res += dfs(node.left, sumVal - node.val)
            res += dfs(node.right, sumVal - node.val)
            return res

        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
