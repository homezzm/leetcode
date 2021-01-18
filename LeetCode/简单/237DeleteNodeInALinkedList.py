# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        https://leetcode-cn.com/problems/delete-node-in-a-linked-list/
        """
        node.val = node.next.val
        node.next = node.next.next
