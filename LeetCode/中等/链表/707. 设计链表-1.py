class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList_1(object):

    def __init__(self):
        """
        Initialize your val structure here.
        """
        self.__dummyHead = ListNode(0)
        self.__size = 0;

    def get(self, index):
        """
        get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index > (self.__size - 1) or index < 0: return -1
        cur = self.__dummyHead.next
        while index:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val):
        """
        addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        newNode = ListNode(val)
        newNode.next = self.__dummyHead.next
        self.__dummyHead.next = newNode
        self.__size += 1

    def addAtTail(self, val):
        """
        addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        newNode = ListNode(val)
        cur = self.__dummyHead
        while cur.next:
            cur = cur.next
        cur.next = newNode
        self.__size += 1

    def addAtIndex(self, index, val):
        """
        addAtIndex(index,val)：在链表中的第index个节点之前添加值为val 的节点。
        如果index等于链表的长度，则该节点将附加到链表的末尾。
        如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.__size: return
        newNode = ListNode(val)
        cur = self.__dummyHead
        while index:
            cur = cur.next
            index-=1
        newNode.next = cur.next
        cur.next = newNode
        self.__size += 1

    def deleteAtIndex(self, index):
        """
        deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index >= self.__size or index < 0: return
        cur = self.__dummyHead
        while index:
            cur = cur.next
            index-=1
        # temp = cur.next
        cur.next = cur.next.next
        self.__size -= 1


from LeetCode.Helpers import *

if __name__ == '__main__':
    linkedList = MyLinkedList_1()

    # ["",  "addAtHead", "get", "get", "get",
    #  "addAtHead", "deleteAtIndex"]
    # [,      [7], [3], [3], [3], [1], [4]]

    linkedList.addAtHead(4)
    linkedList.get(0)
    linkedList.addAtHead(1)
    linkedList.addAtHead(5)
    linkedList.deleteAtIndex(3)

    # print(linkedList.get(0))
    # linkedList.addAtHead(1)
    # linkedList.addAtTail(3)
    # linkedList.addAtIndex(1, 2)  # 链表变为1-> 2-> 3
    # linkedList.get(1)  # 返回2
    # linkedList.deleteAtIndex(1)  # 现在链表是1-> 3
    # print(linkedList.get(1))  # 返回3

    # helperPrintLinkListVal(linkedList.head)
    # print('size:', len(linkedList.stack))
    # for i in linkedList.stack:
    # print(i.val,end='---')
    # print(i)

    #
    #
    #
