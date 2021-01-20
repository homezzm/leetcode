"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/
        :type head: Node
        :rtype: Node
        多级双向链表中，除了指向下一个节点和前一个节点指针之外，
        它还有一个子链表指针，可能指向单独的双向链表。这些子列表也可能会有一个或多个自己的子项，依此类推，
        生成多级数据结构，如下面的示例所示。
        """
        if not head: return head
        pointer, nextPointerList = head, []
        while pointer:
            if pointer.child:
                if pointer.next:
                    nextPointerList.append(pointer.next)
                    pointer.next.prev = None
                pointer.next = pointer.child
                pointer.child.prev = pointer
                pointer.child = None

            if not pointer.next and nextPointerList:
                nextPointer = nextPointerList.pop()
                pointer.next = nextPointer
                if nextPointer:
                    nextPointer.prev = pointer

            pointer = pointer.next
        return head

