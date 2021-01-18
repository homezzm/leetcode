"""
# Definition for a ListNode.
class ListNode(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque


class Solution(object):
    def maxDepth(self, root):
        """
        https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/
        :type root: ListNode
        :rtype: int
        """

        if not root: return 0
        depth, q = 0, deque()
        q.append(root)
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                for c in node.children:
                    q.append(c)
            depth += 1
        return depth

        # 递归写法
        # if not root: return 0
        # depth = 0
        # for i in root.children:
        #     depth = max(depth, self.maxDepth(i))
        # return depth + 1
