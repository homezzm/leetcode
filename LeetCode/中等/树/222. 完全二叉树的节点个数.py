# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        https://leetcode-cn.com/problems/count-complete-tree-nodes/
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        nodeCount = 0

        def dfs(node):
            nonlocal nodeCount
            if node is None: return
            nodeCount += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return nodeCount
