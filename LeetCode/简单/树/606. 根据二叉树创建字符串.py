# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from LeetCode.GenBTreeByList import GenBiTreeByList


class Solution(object):
    def tree2str(self, t):
        """
        https://leetcode-cn.com/problems/construct-string-from-binary-tree/
        :type t: TreeNode
        :rtype: str
        """
        if not t: return ''

        strs = ''

        def pre_order(root):
            nonlocal strs
            if not root: return ''
            strs += str(root.val)

            if root.left or root.right:
                strs += '('
                pre_order(root.left)
                strs += ')'

            if root.right:
                strs += '('
                pre_order(root.right)
                strs += ')'

        pre_order(t)
        return strs
