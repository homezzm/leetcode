# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getDecimalValue(self, head):
        """
        https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer/
        :type head: ListNode
        :rtype: int
        """
        # nums = ''
        # while head:
        #     nums += str(head.val)
        #     head=head.next
        # return int(nums,2)

        sum = 0
        while head:
            sum = sum * 2 + head.val
            head = head.next
        return sum


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(0)
    l3 = ListNode(1)
    l1.next = l2
    l2.next = l3

    solution = Solution()
    print(solution.getDecimalValue(l1))
