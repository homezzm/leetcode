# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        https://leetcode-cn.com/problems/sum-lists-lcci/
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
         716       159补0     9
         592       2367       19要进位
        =219反转   =3858反转   =001
        """
        head = ListNode(0)
        prev, carry = head, 0
        while l1 or l2 or carry > 0:
            valA = l1.val if l1 else 0
            valB = l2.val if l2 else 0
            res = valA + valB + carry  # 7+5
            # result.append(res % 10)  # 12 取 2
            carry = res // 10  # 12 取1
            prev.next = ListNode(res % 10)
            prev = prev.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next


if __name__ == '__main__':
    headA1 = ListNode(9)

    headB1 = ListNode(1)
    headB19 = ListNode(9)
    headB1.next = headB19
    solution = Solution()
    solution.addTwoNumbers(headA1, headB1)

    print(1 // 10)
