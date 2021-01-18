# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        https://leetcode-cn.com/problems/sum-of-nodes-with-even-valued-grandparent/
        :type root: TreeNode
        :rtype: int
        """

        ans = 0

        def dfs(gp_val, p_val, node):  # 祖父值，父值，当前节点
            if not node: return
            if gp_val % 2 == 0:
                nonlocal ans
                ans += node.val
            dfs(p_val, node.val, node.left)
            dfs(p_val, node.val, node.right)

        dfs(1, 1, root)  # 我们可以假设根节点有一个虚拟的祖父节点和父节点，它们的值都为 1
        return ans
