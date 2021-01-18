# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        https://leetcode-cn.com/problems/trim-a-binary-search-tree/
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if not root: return root
        if root.val < low:
            root = root.right  # 拿掉左孩子
            root = self.trimBST(root, low, high)
        elif root.val > high:
            root = root.left  # 拿掉右孩子
            root = self.trimBST(root, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        return root
