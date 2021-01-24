# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        给你一个链表，每k个节点一组进行翻转，请你返回翻转后的链表。
        k是一个正整数，它的值小于或等于链表的长度。
        如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序。

        示例：
        给你这个链表：1->2->3->4->5
        当k= 2 时，应当返回: 2->1->4->3->5
        当k= 3 时，应当返回: 3->2->1->4->5
        """

        if not head or k <= 1: return head
        prev, last, cur = head, head, head

        step = 1
        while cur:
            if step % k == 0:
                while prev != last:
                    dummy = ListNode(-1)
                    temp = prev.next
                    prev.next = dummy

                    dummy.next = prev
                    prev = temp

                prev = last.next

            step += 1
            cur = cur.next
            last = last.next

    def reverseListNode(self, head):  # 反转
        dummy, cur = ListNode(-1), head
        while cur:
            tmp = cur.next
            cur.next = dummy

            dummy = cur
            cur = tmp
        return dummy.next