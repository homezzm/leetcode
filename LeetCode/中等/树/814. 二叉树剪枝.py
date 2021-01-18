# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pruneTree(self, root):
        """
        https://leetcode-cn.com/problems/binary-tree-pruning/
        :type root: TreeNode
        :rtype: TreeNode
        如果当前节点为0，且没有左右节点就剪枝掉
        """
        if root is None: return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and root.left is None and root.right is None:
            return None
        return root
