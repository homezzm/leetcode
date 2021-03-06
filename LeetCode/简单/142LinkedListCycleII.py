# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if head is None: return None
        fast, slow = head, head
        while fast:
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return None
            if fast == slow:
                break

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow