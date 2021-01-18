"""
# Definition for a ListNode.
class ListNode(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
        :type root: ListNode
        :rtype: List[int]
        """
        if not root: return []
        res = []

        def dfs(node, res):
            if not node: return
            res.append(node.val)
            if node.children:
                for childrenNode in node.children:
                    dfs(childrenNode,res)

        dfs(root, res)
        return res
