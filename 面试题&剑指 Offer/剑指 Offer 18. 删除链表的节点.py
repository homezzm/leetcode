# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, head, val):
        """
        https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return
        cur, pre = head, None
        while cur:
            if cur.val == val:
                if pre is None:  # 删除的是头节点
                    cur = head.next
                    return cur
                else:
                    pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6

    solution = Solution()
    cu = solution.deleteNode(l1, 2)
    while cu:
        print(cu.val, end=' ')
        cu = cu.next
