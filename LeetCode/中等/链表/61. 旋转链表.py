#!/usr/bin/env Python
# coding=utf-8
from collections import deque


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        https://leetcode-cn.com/problems/rotate-list/
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return head
        length = 1
        p = head
        while p.next:
            length += 1
            p = p.next

        k = k % length
        if k == 0: return head

        p.next = head  # 成环
        steps = length - k
        while steps > 0:
            p = p.next
            steps -= 1

        newHead = p.next
        p.next = None

        return newHead

    def printLink(self, head):
        while head:
            print(head.val, end='->')
            head = head.next
        print()


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    l1.next = l2
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    solution = Solution()
    res = solution.rotateRight(l1, 2)

    while res:
        print(res.val, end='->')
        res = res.next
