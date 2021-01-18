"""
# Definition for a ListNode.
class ListNode(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def postorder(self, root):
        """
        https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/
        :type root: ListNode
        :rtype: List[int]
        """
        if not root: return []
        res = []

        def dfs(node):
            if not node: return

            if node.children:
                for childrenNode in node.children:
                    dfs(childrenNode)
            res.append(node.val)

        dfs(root)
        return res
