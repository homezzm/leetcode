# Definition for singly-linked list.
from collections import deque


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        https://leetcode-cn.com/problems/add-two-numbers-ii/
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        thinking:把两个列表入列表中，然后从列表的第0个位置开始相加，注意进位，以长列表为准
        """
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry, head = 0, None
        while stack1 or stack2 or carry > 0:
            sumVal = carry
            sumVal += 0 if not stack1 else stack1.pop()
            sumVal += 0 if not stack2 else stack2.pop()
            node = ListNode(sumVal % 10)
            node.next = head
            head = node
            carry = sumVal // 10
        return head


if __name__ == '__main__':
    l7 = ListNode(7)
    l12 = ListNode(2)
    l4 = ListNode(4)
    l3 = ListNode(3)
    l7.next = l12
    l12.next = l4
    l4.next = l3

    ll5 = ListNode(5)
    ll6 = ListNode(6)
    ll4 = ListNode(4)

    ll5.next = ll6
    ll6.next = ll4

    solution = Solution()
    res = solution.addTwoNumbers(l7, ll5)
    while res:
        print(res.val, end=' ')
        res = res.next
