# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


if __name__ == '__main__':
    solution = Solution()
    list1 = ListNode(1)
    list11 = ListNode(1)
    list2 = ListNode(2)
    list1.next = list11
    list11.next = list2
    res = solution.deleteDuplicates(list1)
    while  res:
        print(res.val)
        res = res.next
