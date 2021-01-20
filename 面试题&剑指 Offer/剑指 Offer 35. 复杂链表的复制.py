# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/
        :type head: Node
        :rtype: Node
        请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，
        每个节点除了有一个 next 指针指向下一个节点，
        还有一个 random 指针指向链表中的任意节点或者 null。
        """
        if not head: return head

        dicts = dict() #key是原来的节点对象 value是新的节点对象

        def getNode(oldNode):
            if oldNode in dicts:
                node = dicts[oldNode]
            else:
                node = Node(oldNode.val)
                dicts[oldNode] = node
            return node

        dummyNode = cur = Node(0)
        while head:
            newNode = getNode(head)
            if head.next:
                newNode.next = getNode(head.next)
            if head.random:
                newNode.random = getNode(head.random)

            cur.next = newNode
            cur = newNode

            head = head.next
        return dummyNode.next


if __name__ == '__main__':
    h7 = Node(7)
    h13 = Node(13)
    h11 = Node(11)

    h7.next = h13
    h13.next = h11

    h13.random = h7

    solution = Solution()
    solution.copyRandomList(h7)
