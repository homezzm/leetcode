"""
# Definition for a ListNode.
class ListNode(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque


class Solution(object):
    def connect(self, root):
        """
        https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/
        :type root: ListNode
        :rtype: ListNode
        每个 node 左子树的 next , 就是 node 的右子树
        每个 node 右子树的 next, 就是 node next 的 左子树
        """
        if not root: return

        def dfs(node, next):
            if not node: return
            node.next = next
            dfs(node.left, node.right)
            dfs(node.right, node.next.left if node.next else None)

        dfs(root, None)
        return root


if __name__ == '__main__':
    solution = Solution()
    # solution.connect()
