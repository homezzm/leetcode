# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        poiA, poiB = headA, headB
        # 两个指针要么是都是空，就是两个链表是平行的
        # 要么相等，找到了相遇点
        while poiA != poiB:
            poiA = headB if not poiA else poiA.next
            poiB = headA if not poiB else poiB.next
        return poiA
