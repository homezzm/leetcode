# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        https://leetcode-cn.com/problems/delete-middle-node-lcci/
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next


if __name__ == '__main__':
    l1 = ListNode(4)
    l2 = ListNode(5)
    l3 = ListNode(1)
    l4 = ListNode(9)
    l1.next = l2
    l2.next = l3
    l3.next = l4

    solution = Solution()
    solution.deleteNode(l2)
    while l1:
        print(l1.val)
        l1 = l1.next
