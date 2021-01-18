# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        thinking:first,second两个指针
        两指针初始均为head，first走k步后，first与second同时前进，
        此时如果first为None则second即为所指节点，返回即可
        """
        if not head: return head
        first = second = head
        while first:
            if k > 0:
                first = first.next
                k -= 1
                continue
            first = first.next
            second = second.next
        return second

        # thinking2:使用栈方式，先把所有节点入站，则head会在栈底位置
        # 出栈时使用k弹出指定位置节点并返回即可
        # stack = []
        # while head:
        #     stack.append(head)
        #     head = head.next
        # stack.reverse()
        # return stack.pop(k-1)


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
    res = solution.getKthFromEnd(l1, 4)
    while res:
        print(res.val, end=' ')
        res = res.next
