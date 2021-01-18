# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
        示例：
        输入：1->2->4, 1->3->4
        输出：1->1->2->3->4->4
        """
        dummy_node = ListNode()
        head = dummy_node  # 哑节点
        while l1 and l2:
            if l1.val < l2.val:
                head.next = ListNode(l1.val)
                l1 = l1.next
            else:
                head.next =  ListNode(l2.val)
                l2 = l2.next
            head=head.next
        if l1: head.next = l1
        if l2: head.next = l2
        return dummy_node.next


if __name__ == '__main__':
    onel1_1 = ListNode(1)
    onel1_2 = ListNode(2)
    onel1_4 = ListNode(4)
    onel1_1.next = onel1_2
    onel1_2.next = onel1_4

    twol2_1 = ListNode(1)
    twol2_3 = ListNode(3)
    twol2_4 = ListNode(4)

    twol2_1.next = twol2_3
    twol2_3.next = twol2_4

    solution = Solution()
    head1 = solution.mergeTwoLists(onel1_1, twol2_1)
    while head1:
        print(head1.val)
        head1=head1.next
