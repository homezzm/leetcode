# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        https://leetcode-cn.com/problems/leaf-similar-trees/
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 or not root2: return False
        li1, li2 = [], []

        def dfs(node, li):
            if not node: return
            if not node.left and not node.right:
                li.append(node.val)
            dfs(node.left, li)
            dfs(node.right, li)

        dfs(root1, li1)
        dfs(root2, li2)
        return li1 == li2
