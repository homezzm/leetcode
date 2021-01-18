# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        https://leetcode-cn.com/problems/remove-duplicate-node-lcci/
        :type head: ListNode
        :rtype: ListNode
        """
        set_nums = set()
        curr = head
        while curr:
            if curr.val in set_nums:
                pre.next = pre.next.next
                curr = pre.next
            else:
                set_nums.add(curr.val)
                pre = curr
                curr = curr.next

        return head

if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(3)
    l5 = ListNode(2)
    l6 = ListNode(1)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6

    solution = Solution()
    cu=solution.removeDuplicateNodes(l1)
    while cu:
        print(cu.val)
        cu=cu.next
