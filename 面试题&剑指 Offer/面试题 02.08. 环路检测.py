# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        https://leetcode-cn.com/problems/linked-list-cycle-lcci/
        :type head: ListNode
        :rtype: ListNode
        1.快慢指针，快走1慢走2，相遇即有环
        2.相遇后，快指针回到头部，与慢指针一步一步走，再次相遇即为入口点，返回即可
        3.注意要增加一个头节点，如有情况1->2->1 这样的一个环形如果没有头节点将会出错
        """
        if not head:return head
        dummy = ListNode(0)
        dummy.next = head

        slow, fast, isExistsCycle = dummy, dummy, False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = dummy
                isExistsCycle = True
                break

        if not isExistsCycle:
            return None
        while fast:
            slow = slow.next
            fast = fast.next
            if slow == fast:
                break
        return slow


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l1.next = l2
    #l2.next = l1

    solution = Solution()
    res = solution.detectCycle(l1)
    print(res)
