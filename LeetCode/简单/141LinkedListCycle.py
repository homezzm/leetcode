# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    https://leetcode-cn.com/problems/linked-list-cycle/
    """
    def hasCycle(self, head):
        if head is None: return False
        fast, slow = head, head
        while fast:
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return False
            if fast == slow:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
