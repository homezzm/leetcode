# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        https://leetcode-cn.com/problems/middle-of-the-linked-list/
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        # stack = []
        # while head:
        #     stack.append(head)
        #     head = head.next
        #
        # return stack[len(stack) // 2]

        # 快慢指针
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


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
    head = solution.middleNode(l1)

    while head:
        print(head.val)
        head = head.next
