# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/
        :type root: TreeNode
        :type k: int
        :rtype: int
        给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
        """
        res = count = 0

        def inOrder(node):
            nonlocal res, count
            if not node: return
            inOrder(node.left)
            count += 1
            if count == k:
                res = node.val
                return
            inOrder(node.right)

        inOrder(root)
        return res
