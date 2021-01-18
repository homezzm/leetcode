# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        https://leetcode-cn.com/problems/swap-nodes-in-pairs/
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        pre = ListNode(0)
        pre.next = head

        p = pre
        while p.next and p.next.next:
            node1 = p.next
            node2 = p.next.next  # node1.next

            p.next = node2
            node1.next = node2.next

            node2.next = node1

            p = node1
        return pre.next
