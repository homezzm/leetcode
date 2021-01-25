# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
        讲解：https://www.bilibili.com/video/BV1SD4y197TK?from=search&seid=14961171138606591985
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
        tail = head
        for i in range(k):  # 找到链表尾所在位置k=3 tail=4
            if not tail: return head  # 链表的最后一段不够k的长度，就直接返回，不翻转了
            tail = tail.next
        # 1->2->3 to 3->2->1
        #           |     |
        #        newHead head
        newHead = self.reverseListNode(head, tail)  # 翻转这个区域的链表
        head.next = self.reverseKGroup(tail, k)  # 从1的这个位置继续往后操作4-5
        return newHead

    def reverseListNode(self, head, tail):
        prev = None
        while head != tail:
            tmp = head.next
            head.next = prev

            prev = head
            head = tmp
        return prev
