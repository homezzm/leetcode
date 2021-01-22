# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        https://leetcode-cn.com/problems/copy-list-with-random-pointer/
        :type head: Node
        :rtype: Node
        给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
        """

        dicts = dict()  # 保存所有创建的对象 k是旧节点 v是新节点

        def getNode(oriNode):
            if oriNode in dicts:
                return dicts[oriNode]
            newNode = Node(oriNode.val)
            dicts[oriNode] = newNode
            return newNode

        dummy = Node(0)
        newHead = dummy
        while head:
            node = getNode(head)
            if head.next:
                node.next = getNode(head.next)
            if head.random:
                node.random = getNode(head.random)
            dummy.next = node
            dummy = node
            head = head.next

        return newHead.next
