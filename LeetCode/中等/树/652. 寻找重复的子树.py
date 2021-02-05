# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter


class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        https://leetcode-cn.com/problems/find-duplicate-subtrees/
        :type root: TreeNode
        :rtype: List[TreeNode]
        给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
        两棵树重复是指它们具有相同的结构以及相同的结点值。
        """

        if not root: return []
        counter, res = Counter(), []

        def dfs(node):
            if not node: return '#'

            leftVal = dfs(node.left)
            rightVal = dfs(node.right)
            subTree = str(node.val) + ',' + str(leftVal) + ',' + str(rightVal)

            counter[subTree] += 1
            if counter[subTree] == 2:
                res.append(node)
            return subTree

        dfs(root)
        return res
