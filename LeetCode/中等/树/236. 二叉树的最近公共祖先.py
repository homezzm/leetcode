# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """



        def dfs(node):
            if not node or node == p or node == q: return node  # 当 root 等于p, q则直接返回 root

            left = dfs(node.left)  # 开启递归左子节点，返回值记为 left
            right = dfs(node.right)  # 开启递归右子节点，返回值记为 right

            # 当 left 为空 ，right 不为空 ：p,q 都不在 root 的左子树中，直接返回 right 。
            if not left: return right

            # 当 left 不为空 ， right 为空
            if not right: return left

            # 当 left 和 right 同时不为空 ：说明p, q分列在 root的 异侧 （分别在 左 / 右子树），
            # 因此 root 为最近公共祖先，返回 root ；
            return node

        return dfs(root)
