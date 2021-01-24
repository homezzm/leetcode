# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        https://leetcode-cn.com/problems/check-balance-lcci/
        :type root: TreeNode
        :rtype: bool
        实现一个函数，检查二叉树是否平衡。在这个问题中，
        平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。
        """
        if not root: return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and \
               abs(self.depth(root.left) - self.depth(root.right)) <= 1

    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
