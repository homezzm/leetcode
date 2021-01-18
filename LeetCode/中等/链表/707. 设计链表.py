# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your val structure here.
        """
        self.stack = []
        self.head = None  # 链表头

    def get(self, index):
        """
        get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if len(self.stack)-1 < index:
            return -1
        return self.stack[index].val

    def addAtHead(self, val):
        """
        addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new_head = ListNode(val)
        if not self.head:  # 空头
            self.head = new_head
        else:
            new_head.next = self.head
            self.head = new_head  # 更新头
        self.stack.insert(0, new_head)

        # new_head = ListNode(val)
        # new_head.next = self.head
        # self.head = new_head  # 更新头
        # self.stack.insert(0, new_head)

    def addAtTail(self, val):
        """
        addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if not self.head:#头是空的
            self.addAtHead(val)

        last_node = ListNode(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = last_node
        self.stack.append(last_node)

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
        n = len(self.stack)
        if index == n:  # 如果index等于链表的长度，则该节点将附加到链表的末尾。
            if n == 0:  # 现在有没有链表节点就直接插入到头里
                self.addAtHead(val)
            else:
                self.addAtTail(val)
        elif index < 0:
            self.addAtHead(val)  # 如果index小于0，则在头部插入节点。
        elif index > n:  # 如果 index 大于链表长度，则不会插入节点。
            return
        else:  # 在链表指定位置插入
            # 如果插入的位置是0，且已存在头，替换其值即可
            if index == 0 and self.head:
                self.head.val = val
                return

            ins_node = ListNode(val)
            cur, pre = self.head, ListNode('empty')
            while cur:
                cur_index = self.stack.index(cur)
                if cur_index == index:
                    temp = cur
                    pre.next = ins_node
                    ins_node.next = temp
                    self.stack.insert(index, ins_node)
                    if cur_index == 0:  # 插入的是头就需要更新下头
                        self.head = ins_node
                    break
                pre = cur
                cur = cur.next

    def deleteAtIndex(self, index):
        """
        deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if len(self.stack)-1 < index: return
        pre = ListNode(-1)  # 哨兵节点
        pre.next, cur = self.head, self.head

        del_node = self.stack[index]  # 找到这个对象
        while cur:
            if cur == del_node:
                pre.next = cur.next
                self.stack.remove(del_node)
                break
            pre = cur
            cur = cur.next


from LeetCode.Helpers import *

if __name__ == '__main__':
    linkedList = MyLinkedList()

    # ["",  "addAtHead", "get", "get", "get",
    #  "addAtHead", "deleteAtIndex"]
    # [,      [7], [3], [3], [3], [1], [4]]

    linkedList.addAtHead(4)
    linkedList.get(0)
    linkedList.addAtHead(1)
    linkedList.addAtHead(5)
    linkedList.deleteAtIndex(3)





    #print(linkedList.get(0))
    # linkedList.addAtHead(1)
    # linkedList.addAtTail(3)
    # linkedList.addAtIndex(1, 2)  # 链表变为1-> 2-> 3
    # linkedList.get(1)  # 返回2
    # linkedList.deleteAtIndex(1)  # 现在链表是1-> 3
    # print(linkedList.get(1))  # 返回3

    helperPrintLinkListVal(linkedList.head)
    print('size:', len(linkedList.stack))
    # for i in linkedList.stack:
    # print(i.val,end='---')
    # print(i)

    #
    #
    #
