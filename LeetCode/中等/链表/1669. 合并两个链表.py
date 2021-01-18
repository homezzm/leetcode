# Definition for singly-linked list.
from LeetCode.Helpers import helperPrintLinkListVal


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        https://leetcode-cn.com/problems/merge-in-between-linked-lists/
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        1.先找到list1中要删除的a的位置 使用dummy节点记录要删除a位置的前一个位置
        2.记录下dummy节点的对象后，继续遍历找到list1结束删除的b位置的.next节点并记录
        3.找到list2的结尾节点
        4.dummy.next=list2   list2的结尾节.next=list1的b位置.next节点
        list2有可能 是一个 list1最少三个
        """
        nodeBegin, nodeEnd = list1, list1
        for i in range(a - 1):
            nodeBegin = nodeBegin.next
        for i in range(b):
            nodeEnd = nodeEnd.next

        node2End = list2
        while node2End.next:
            node2End = node2End.next

        nodeBegin.next = list2
        if nodeEnd:
           node2End.next = nodeEnd.next
        return list1

        # 以下代码太恶心，我要吐了
        # l1Begin, l1End = None, None
        # dummy = ListNode(-1)
        # dummy.next = list1
        # i = 0
        # while dummy:
        #     if i == a:
        #         l1Begin = dummy
        #     elif i == b:
        #         l1End = dummy.next
        #         break
        #     dummy = dummy.next
        #     i += 1
        #
        # l2End = list2
        # while l2End.next:
        #     l2End = l2End.next
        #
        # l1Begin.next = list2
        # l2End.next = l1End.next
        # #helperPrintLinkListVal(list1)
        # return list1


if __name__ == '__main__':
    l1 = ListNode(0)
    l2 = ListNode(1)
    l3 = ListNode(2)
    l4 = ListNode(3)
    l5 = ListNode(4)
    l6 = ListNode(5)
    l7 = ListNode(6)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    # l6.next = l7

    l100000 = ListNode(100000)
    l200001 = ListNode(100001)
    l300001 = ListNode(100002)
    l400001 = ListNode(100003)
    l500001 = ListNode(100004)
    l100000.next = l200001
    l200001.next = l300001
    # l300001.next = l400001
    # l400001.next = l500001

    solution = Solution()
    solution.mergeInBetween(l1, 3, 4, l100000)
