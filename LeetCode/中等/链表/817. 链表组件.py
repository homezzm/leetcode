# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def numComponents(self, head, G):
        """
        https://leetcode-cn.com/problems/linked-list-components/
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        if not head: return
        num_set = set(G)
        count = 0
        while head:
            if head.val in num_set and (not head.next or head.next.val not in num_set):
                count += 1
            head = head.next
        return count

if __name__ == '__main__':
    l1 = ListNode(0)
    l2 = ListNode(1)
    l3 = ListNode(2)
    l4 = ListNode(3)
    l5 = ListNode(4)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    solution = Solution()
    print(solution.numComponents(l1, [0, 3, 1, 4]))
