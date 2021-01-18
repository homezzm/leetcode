# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        https://leetcode-cn.com/problems/validate-binary-search-tree/
        :type root: TreeNode
        :rtype: bool
        给定一个二叉树，判断其是否是一个有效的二叉搜索树。
        thinking:中序遍历，看下是否是递增即可
        """
        pre = float('-inf')

        def inOrder(node):
            nonlocal pre
            if not node: return True

            if not inOrder(node.left): return False
            if pre >= node.val:  return False
            pre = node.val

            return inOrder(node.right)

        return inOrder(root)
