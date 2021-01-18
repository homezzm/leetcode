# 链表
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# 头插法
def create_linklist_head(li):
    head = ListNode(li[0])  # 头节点
    # 列表从1开始切片，切到最后，因为第一个头元素已经插入了
    for element in li[1:]:
        node = ListNode(element)
        node.next = head  # 3.next = 2  # 3与2进行链接
        head = node  # head=3   #把头指向3
        # 由于链表不是顺序存储的，所以不存在后续元素移动的问题
    return head  # 返回链表头


# 尾插法，要知道头也要知道尾
def create_linklist_tail(li):
    head = ListNode(li[0])  # 头节点
    tail = head  # 初始时头即尾，尾即头
    for element in li[1:]:
        node = ListNode(element)
        tail.next = node
        tail = node
    return head


def print_linklist(lk):
    while lk:
        print(lk.item, end=',')
        lk = lk.next


lk_head = create_linklist_head([1, 2, 3])
lk_tail = create_linklist_tail([1, 2, 3])
print_linklist(lk_head)
print()
print_linklist(lk_tail)
