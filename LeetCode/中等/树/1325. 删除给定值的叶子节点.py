# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        https://leetcode-cn.com/problems/delete-leaves-with-a-given-value/
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        后序遍历，匹配target即删除
        """

        if not root: return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        if not root.left and not root.right and root.val == target:
            return None
        return root
