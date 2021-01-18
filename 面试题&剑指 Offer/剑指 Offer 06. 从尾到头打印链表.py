# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reversePrint(self, head):
        """
        https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
        :type head: ListNode
        :rtype: List[int]
        """
        cur, pre = head, None
        while cur:
            temp = cur.next
            cur.next = pre

            pre = cur
            cur = temp

        li = []
        while pre:
            li.append(pre.val)
            pre = pre.next
        return li

        # li = []
        # cur = head
        # while cur:
        #     li.append(cur.val)
        #     cur = cur.next
        # li.reverse()
        # return li


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3

    solution = Solution()
    print(solution.reversePrint(l1))
