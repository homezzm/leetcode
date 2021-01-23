# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        https://leetcode-cn.com/problems/reverse-linked-list-ii/
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
        输入: 1->2->3->4->5->NULL, m = 2, n = 4
        输出: 1->4->3->2->5->NULL
        thinking:
        1.首先根据方法的参数m确定g和p的位置。将g移动到第一个要反转的节点的前面，
        将p移动到第一个要反转的节点的位置上。
        2.将p后面的元素删除，然后添加到g的后面。也即头插法。
        """

        if not head or m >= n: return head

        dummy = ListNode(0)
        dummy.next = head
        first, second, step = dummy, head, 0
        while step < m-1:
            first = first.next
            second = second.next
            step+=1

        step=0
        while step<n-m:
            removeNode = second.next #3
            second.next=second.next.next #2->4

            removeNode.next = first.next
            first.next = removeNode
            step+=1
        return dummy.next

