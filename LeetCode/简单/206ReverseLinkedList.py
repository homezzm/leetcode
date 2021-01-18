# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        https://leetcode-cn.com/problems/reverse-linked-list/
        """
        oldNode = head
        newNode = None
        while oldNode:
            oldNextNode = oldNode.next
            oldNode.next = newNode
            newNode = oldNode
            oldNode = oldNextNode
        return newNode
