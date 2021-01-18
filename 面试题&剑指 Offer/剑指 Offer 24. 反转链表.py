# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
        :type head: ListNode
        :rtype: ListNode
        """
        cur, pre = head, None
        while cur:
            # 保存下一节点
            temp = cur.next

            # 将当前节点指向pre 翻转操作
            cur.next = pre

            #继续移动pre和cur指针
            pre = cur
            cur = temp
            # cur.next,pre,cur=pre,cur,cur.next
        return pre


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4

    solution = Solution()
    h = solution.reverseList(l1)
    while h:
        print(h.val, end=' ')
        h = h.next
