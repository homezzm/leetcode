# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def insertIntoBST(self, root, val):
        """
        https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root: return TreeNode(val)

        def dfs(node):
            if not node:
                return TreeNode(val)
            if val <= node.val:
                node.left = dfs(node.left)
            else:
                node.right = dfs(node.right)
            return node
            # 下面是第一版
            # if not node: return
            # if val >= node.val: #5>4
            #     if not node.right: #False
            #         node.right = TreeNode(val)
            #     else:
            #         dfs(node.right)
            #
            # elif val <= node.val:
            #     if not node.left:
            #         node.left = TreeNode(val)
            #     else:
            #         dfs(node.left)

        dfs(root)
        return root
