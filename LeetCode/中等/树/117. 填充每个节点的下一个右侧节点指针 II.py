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
        https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/
        :type root: ListNode
        :rtype: ListNode
        层次遍历，先右后左，每次都保存右边的节点，然后把当前节点指向右边即可
        """

        if not root: return root
        q = deque()
        q.append(root)

        while q:
            n = len(q)
            lastOneNode = None  # 后一个节点
            for _ in range(n):
                node = q.popleft()

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

                if lastOneNode:
                    node.next = lastOneNode
                lastOneNode = node
        return root
