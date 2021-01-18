# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        https://leetcode-cn.com/problems/palindrome-linked-list-lcci/
        :type head: ListNode
        :rtype: bool
        1，采用快慢指针去寻找链表的中间节点；
        2，根据链表的中间节点反转后一半的链表；
        3，迭代比较链表前一半的元素和后一半的元素，判断节点的值是否相等，得出是否为回文。
        """

        slow = fast = head  # slow即是中间点
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        cur, pre = slow, None  # 反转后pre即是第二部分反转后的链表
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        curr1, curr2 = head, pre  # 两开始对比
        while curr1 and curr2:
            if curr1.val == curr2.val:
                curr1 = curr1.next
                curr2 = curr2.next
            else:
                return False
        return True


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(3)
    l5 = ListNode(2)
    l6 = ListNode(1)
    l7 = ListNode(0)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = l7

    solution = Solution()
    print(solution.isPalindrome(l1))
