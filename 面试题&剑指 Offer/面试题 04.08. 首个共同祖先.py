# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        https://leetcode-cn.com/problems/first-common-ancestor-lcci/
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。
        不得将其他的节点存储在另外的数据结构中。注意：这不一定是二叉搜索树。
        """

        if not root or root == q or root == p: return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left: return right
        if not right: return left

        return root
