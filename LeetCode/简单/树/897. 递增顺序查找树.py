# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from LeetCode.GenBTreeByList import GenBiTreeByList


class Solution(object):
    def increasingBST(self, root):
        """
        https://leetcode-cn.com/problems/increasing-order-search-tree/
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = []

        def dfs(node):
            if not node: return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        ans = cur = TreeNode(None)
        for i in res:
            cur.right = TreeNode(i)
            cur = cur.right
        return ans.right
