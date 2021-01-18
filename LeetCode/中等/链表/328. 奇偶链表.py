# Definition for singly-linked list.
from LeetCode.Helpers import helperPrintLinkListVal


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        https://leetcode-cn.com/problems/odd-even-linked-list/
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        even, odd = head.next, head
        even_head, odd_head = even, odd  # even=2 odd=1

        while even and even.next:
            odd.next = even.next
            odd = even.next
            even.next = odd.next
            even = odd.next

        odd.next = even_head
        head = odd_head
        return head
        # helperPrintLinkListVal(head)


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    # l4.next = l5

    solution = Solution()
    solution.oddEvenList(l1)
