# Definition for singly-linked list.
from LeetCode.Helpers import helperPrintLinkListVal


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        if not head or not head.next:
            return head

        slow, fast = head, head
        while fast.next and fast.next.next:  # 用快慢指针分成两部分
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None  # 找到左右部分, 把左部分最后置空，链表断开是重点

        left = self.sortList(head)  # 递归下去
        right = self.sortList(mid)

        return self.merge(left, right)  # 合并

    def merge(self, left, right):
        dummy = ListNode(0)
        p = dummy
        l = left
        r = right

        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
                p = p.next
            else:
                p.next = r
                r = r.next
                p = p.next
        if l:
            p.next = l
        if r:
            p.next = r
        return dummy.next

    # def sortList(self, head):
    #     """
    #     https://leetcode-cn.com/problems/sort-list/
    #     :type head: ListNode
    #     :rtype: ListNode
    #     归并排序
    #     """
    #     if not head: return head
    #
    #     self.merge_sort(head, None, None)
    #     helperPrintLinkListVal(head)
    #
    # def merge_sort(self, head, low, high):
    #     # 快慢指针找到中间位置
    #     slow, fast, mid = low, low, None
    #     if not low:
    #         slow, fast = head, head
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next
    #
    #     low, mid, high = head, slow, fast
    #     print('low:',low.val,'  mid:',mid.val)
    #
    #     if low and mid:
    #         self.merge_sort(head, low, mid)
    #         self.merge_sort(head, mid.next, high)
    #         self.merge(head, low, mid)
    #
    # def merge(self, head, low, mid):
    #
    #     while low and mid:
    #         if low.val < mid.val:
    #             head.next = low
    #             low = low.next
    #         else:
    #             head.next = mid
    #             mid = mid.next
    #         head = head.next
    #
    #     while low:
    #         head.next = low
    #         low = low.next
    #         head = head.next
    #     while mid:
    #         head.next = mid
    #         mid = mid.next
    #         head = head.next


if __name__ == '__main__':
    l1 = ListNode(4)
    l2 = ListNode(2)
    l3 = ListNode(1)
    l4 = ListNode(3)
    l5 = ListNode(5)
    # l6 = ListNode(6)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    # l5.next = l6

    solution = Solution()
    #solution.sortList(l1)

    print(chr(20851),chr(27880),chr(25105))