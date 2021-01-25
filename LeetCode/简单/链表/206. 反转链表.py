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
        if not head: return head
        pre = None
        while head:
            tmp = head.next
            head.next = pre

            pre = head
            head = tmp
        return pre
