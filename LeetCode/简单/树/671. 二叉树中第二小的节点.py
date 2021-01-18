# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/
        :type root: TreeNode
        :rtype: int
        已知第一小的节点值为root.val
        """
        setNode, min1 = set(), root.val

        def dfs(node):
            if not node: return

            if node.val > min1:  # 如果当前节点小于min1就代表整颗子树都小于他
                setNode.add(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return min(setNode) if len(setNode) else -1

