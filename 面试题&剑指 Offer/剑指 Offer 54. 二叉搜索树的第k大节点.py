# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/
        :type root: TreeNode
        :type k: int
        :rtype: int
        中序遍历取倒数k个数即可
        """
        def inOrder(node):
            return inOrder(node.left) + [node.val] + inOrder(node.right) if node else []
        return inOrder(root)[:-k]

