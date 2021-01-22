# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
        进阶：你能尝试使用一趟扫描实现吗？
        增加哑节点，初始时慢指针指向哑节点，快指针指向头节点，依然是快先走k步，然后快慢一起走，但指向哑节点有个好处是，当快指针走不了的时候，慢指针是指向被删除节点的前驱节点的。
        """
        # 从官方那学的
        dummy = ListNode(0, head)
        slow, fast = dummy, head
        while fast:
            if n:
                fast = fast.next  # 快递指针先走N步
                n -= 1
                continue
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

        #
        # if not head or n <= 0: return head
        # slow, fast = head, head
        # while fast:
        #     if n:
        #         fast = fast.next  # 快递指针先走N步
        #         n -= 1
        #         continue
        #     slow = slow.next
        #     fast = fast.next
        #
        # # 三种情况，1.删除节点在头 2.删除节点在尾 3.删除节点在中间
        # if slow.next:  # 1.删除节点在头 3.删除节点在中间
        #     slow.val = slow.next.val
        #     slow.next = slow.next.next
        # elif slow == head:  # 要删除的k节点与头节点相同，那表示链表中只有一个节点
        #     head = None
        # else:  # 2.删除节点在尾
        #     curNode = head
        #     while curNode:
        #         if curNode.next == slow:  # 找到尾巴
        #             curNode.next = None
        #         curNode = curNode.next
        #
        # return head
