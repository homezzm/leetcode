# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return None
        if p.val == q.val:
            return p
        while root:
            if root.val < q.val and root.val < p.val:
                root = root.right
            if root.val > q.val and root.val > p.val:
                root = root.left
            else:
                return root


        # def dfs(node):
        #     if not node or node == q or node == p: return node
        #
        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #
        #     if not left: return right
        #     if not right: return left
        #
        #     return node
        # return dfs(root)
