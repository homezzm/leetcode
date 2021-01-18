# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        https://leetcode-cn.com/problems/subtree-of-another-tree/
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        套路模板
        """

        if t is None: return True
        if s is None: return False

        def dfs(node1, node2):
            if node1 is None and node2 is None: return True #主子树都没有了就代表有子树
            if node1 is None or node2 is None: return False #有一个先为空就代表没有了
            if node1.val != node2.val: return False
            # 比对完一次后在看看左边和右边是不是一样的
            return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)

        return dfs(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
