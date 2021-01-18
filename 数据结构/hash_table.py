# 哈希表
# 先实现哈希中的链表
class LinkList:
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.val
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None  # 头
        self.tail = None  # 尾
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s  # 用的尾插
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
            else:
                return False

    def __iter__(self):  # 让该类支持for循环
        return self.LinkListIterator(self.head)

    def __repr__(self):  # ToString()
        return "<<" + ",".join(map(str, self)) + ">>"


class HashTable:
    def __init__(self, size=101):  # size哈希表大小
        self.size = size
        # [None for i in range(self.size)]
        self.T = [LinkList() for i in range(self.size)]

    def h(self, k):  # 哈希函数
        return k % self.size

    def insert(self, k):
        i = self.h(k)  # 使用哈希函数计算出k应该保存的位置
        # 类似集合的结构，集合是可以重复的，所以要插入前要先查找
        if self.find(k):
            print("重复插入")
        else:
            self.T[i].append(k)

    def find(self, k):
        # 如果k存在，那一定是在i这个位置的链表中
        i = self.h(k)  # 使用哈希函数计算出k应该保存的位置
        return self.T[i].find(k)


if __name__ == '__main__':
    ht = HashTable()
    ht.insert(0)
    ht.insert(1)
    ht.insert(3)
    ht.insert(102)
    print(",".join(map(str,ht.T)))
