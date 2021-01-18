# Definition for singly-linked list.
from LeetCode.Helpers import *


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        a, b = dummy, head
        while b and b.next:
            if a.next.val != b.next.val:
                a = a.next
                b = b.next
            else:
                while b and b.next and a.next.val == b.next.val:
                    b = b.next
                a.next = b.next
                b = b.next
        #helperPrintLinkListVal(dummy.next)
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(1)
    l3 = ListNode(1)
    l4 = ListNode(2)
    l5 = ListNode(2)

    l6 = ListNode(4)
    l7 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    # l5.next = l6
    # l6.next = l7

    solution = Solution()
    solution.deleteDuplicates(l1)
