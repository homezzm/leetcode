# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        https://leetcode-cn.com/problems/binary-tree-tilt/
        其实就是左子树+右子树+根的和
        注意，叶子节点以0计算
        """

        if not root: return 0
        sumVal = 0

        def dfs(node):
            nonlocal sumVal
            if not node: return 0  # 叶子节点以0计算
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            sumVal += abs(leftSum - rightSum)
            return node.val + leftSum + rightSum

        dfs(root)
        return sumVal
