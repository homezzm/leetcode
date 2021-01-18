# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        """
        https://leetcode-cn.com/problems/reorder-list/
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head: return

        li = []
        temp = head
        while temp:
            li.append(temp)
            temp = temp.next

        half=len(li) // 2
        for i in range(half):
            li[i].next = li[~i]
            li[~i].next = li[i + 1]
        li[half].next = None
        return li[0]

        # 以下代码力扣过不去，超时
        # if not head or not head.next or not head.next.next: return  # 至少保证有三个值
        #
        # node3, node2, node1 = head, None, head
        # while node3.next:
        #     node2 = node3
        #     node3 = node3.next
        #
        # sec = head.next
        # node1.next = node3
        # node3.next = sec
        # node2.next = None
        #
        # self.reorderList(sec)


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    # l5.next = l6

    solution = Solution()
    solution.reorderList(l1)
    while l1:
        print(l1.val, end=' ')
        l1 = l1.next
