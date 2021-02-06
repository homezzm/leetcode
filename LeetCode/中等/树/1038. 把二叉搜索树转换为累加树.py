# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def bstToGst(self, root):
        """
        https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/
        :type root: TreeNode
        :rtype: TreeNode
        给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
        使每个节点 node的新值等于原树中大于或等于node.val的值之和。
        """
        sumVal = 0

        def dfs(node):
            nonlocal sumVal
            if not node: return
            dfs(node.right)
            sumVal = node.val + sumVal
            node.val = sumVal
            dfs(node.left)

        dfs(root)
        return root

if __name__ == '__main__':
    root = TreeNode(val=1, left=TreeNode(val=0, left=None, right=None), right=TreeNode(val=2, left=None, right=None))
    solution = Solution()
    solution.bstToGst(root) 