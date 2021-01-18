# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        https://leetcode-cn.com/problems/intersection-of-two-linked-lists-lcci/
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        posA, posB = headA, headB
        while posA != posB:
            posA = headB if not posA else posA.next
            posB = headA if not posB else posB.next
        return posA
