# Definition for singly-linked list.
from LeetCode.Helpers import helperPrintLinkListVal


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        https://leetcode-cn.com/problems/add-two-numbers/
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry, sumVal, head = 0, 0, ListNode(0)
        cur = head
        while l1 or l2 or carry > 0:
            sumVal += 0 if not l1 else l1.val
            sumVal += 0 if not l2 else l2.val
            sumVal += carry
            carry = sumVal // 10  # 记录进位
            # 用尾插入法
            newNode = ListNode(sumVal % 10)
            head.next = newNode
            head = newNode
            sumVal = 0
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return cur.next
        #helperPrintLinkListVal(cur.next)

        # print(l1.val, ' + ', l2.val)
        # l1 = l1.next
        # l2 = l2.next

        # list1 = self.toList(l1)
        # list2 = self.toList(l2)
        # carry, sumVal, head = 0, 0, ListNode(0)
        # cur = head
        # while len(list1) > 0 or len(list2) > 0 or carry > 0:
        #     sumVal += 0 if len(list1) == 0 else list1.pop()
        #     sumVal += 0 if len(list2) == 0 else list2.pop()
        #     sumVal += carry
        #     carry = sumVal // 10  # 记录进位
        #     # 用尾插入法
        #     newNode = ListNode(sumVal % 10)
        #     head.next = newNode
        #     head = newNode
        #     sumVal = 0
        #
        # #helperPrintLinkListVal(cur.next)
        # return cur.next

    # def toList(self, head):
    #     cur, li = head, [],
    #     while cur:
    #         li.append(cur.val)
    #         cur = cur.next
    #     li.reverse()
    #     return li


if __name__ == '__main__':
    l1 = ListNode(9)
    l2 = ListNode(9)
    # l3 = ListNode(3)
    l1.next = l2
    # l2.next = l3

    ll5 = ListNode(9)
    ll6 = ListNode(6)
    ll4 = ListNode(4)
    # ll5.next = ll6
    # ll6.next = ll4

    solution = Solution()
    #print(solution.addTwoNumbers(l1, ll5))
 