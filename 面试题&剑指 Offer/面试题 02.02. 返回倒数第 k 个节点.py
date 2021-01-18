# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def kthToLast(self, head, k):
        """
        https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci/
        :type head: ListNode
        :type k: int
        :rtype: int
        thinking:两指针
     找到链表中倒数第K个节点，链表为1->2->3->4->5 倒数第k个节点即为4。可采用双指针游走方式。
    初始时first,second两个均指向表头，先让first走k步，然后first与second两个指针同时前进，
    此时如果first指向空，则second即为倒数第k个节点
        """
        first = second = head
        while first:
            if k > 0:
                first = first.next
                k -= 1
                continue
            first = first.next
            second = second.next
        return second.val


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    solution = Solution()
    res = solution.kthToLast(l1, 2)
    print(res)
