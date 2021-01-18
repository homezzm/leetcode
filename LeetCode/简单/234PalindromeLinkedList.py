# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse(self, head):
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def isPalindrome(self, head):
        """
        https://leetcode-cn.com/problems/palindrome-linked-list/
        """
        if not head or not head.next: return True
        # 快慢指针，快走1慢走2，快走完，慢中间
        fast, slow, prev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        prev.next = None

        if not fast:  # 偶数表
            slow = self.reverse(slow)
        else:  # 奇数表
            next_node = slow.next
            slow.next = None
            slow = self.reverse(next_node)

        while head:
            if slow.val != head.val: return False
            slow = slow.next
            head = head.next
        return True
