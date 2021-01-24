# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapNodes(self, head, k):
        """
        https://leetcode-cn.com/problems/swapping-nodes-in-a-linked-list/
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        给你链表的头节点 head 和一个整数 k 。
        交换 链表正数第 k 个节点和倒数第 k 个节点的【值】后，返回链表的头节点（链表 从 1 开始索引）。
        输入：head = [1,2,3,4,5], k = 2
        输出：[1,4,3,2,5]
        """
        if not head or k <= 0: return head

        cur, before, after, step = head, head, head, 0
        while cur.next:
            if step < k - 1:
                before = before.next
            else:
                after = after.next
            step += 1
            cur = cur.next

        # # 找到倒的K值，把after赋上值
        # step = 0
        # while before:
        #     before = before.next
        #     if step >= k:
        #         after = after.next
        #     step += 1
        #
        # # 找到正的k值 把pre和before都赋上值
        # before, step = head, 1
        # while step < k:
        #     before = before.next
        #     step += 1

        # 开始互换值
        before.val, after.val = after.val, before.val
        return head
