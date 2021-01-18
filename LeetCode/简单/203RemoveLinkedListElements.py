# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        https://leetcode-cn.com/problems/remove-linked-list-elements/
        """
        sentinel = ListNode(0)
        sentinel.next = head
        curr, prev = head, sentinel
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return sentinel.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l6 = ListNode(6)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6_1 = ListNode(6)

    l1.next = l2
    l2.next = l6
    l6.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6_1

    solution = Solution()
    final_head = solution.removeElements(l1, 6)
    while final_head:
        print(final_head.val)
        final_head = final_head.next
