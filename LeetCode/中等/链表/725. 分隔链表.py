# Definition for singly-linked list.
from cffi.backend_ctypes import xrange


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def splitListToParts(self, root, k):
        """
        https://leetcode-cn.com/problems/split-linked-list-in-parts/
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        total_len = 0
        cur = root
        while cur:
            total_len += 1
            cur = cur.next
        length = total_len // k  # 每段的基础长度
        m = total_len % k  # 前 l 段需要在基础长度上+1

        res = []
        cur = root
        for i in range(k):
            res.append(cur)
            size = length + (1 if m > 0 else 0)  # 算出每段的长度
            if cur:  # 这里判断cur是否存在，防止cur.next不存在报错
                for j in range(size - 1):
                    cur = cur.next
                m -= 1
                tmp = cur.next  # 把后面一段截掉，后面一段需在后面继续划分
                cur.next = None
                cur = tmp
        return res
        # cur, listLen = root, 0
        # while cur:
        #     listLen += 1
        #     cur = cur.next
        #
        # merchant = listLen // k  # 每个部分的长度
        # remainder = listLen % k  # 多出来的
        # li, cur = [], root
        # if k >= listLen:
        #     while k > 0:
        #         li.append(cur if cur else None)
        #         if cur:
        #             temp = cur.next
        #             cur.next = None
        #             cur = temp
        #         k -= 1
        # else:
        #     while listLen:
        #         n = merchant + remainder
        #         listLen -= (merchant + remainder)
        #         remainder, subLi = 0, []
        #         while n > 0:
        #             li.append(root)
        #             n -= 1
        #             root = root.next
        # return li


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)
    l7 = ListNode(7)
    l8 = ListNode(8)
    l9 = ListNode(9)
    l10 = ListNode(10)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    # l4.next = l5
    # l5.next = l6
    # l6.next = l7
    # l7.next = l8
    # l8.next = l9
    # l9.next = l10

    solution = Solution()
    solution.splitListToParts(l1, 5)
