class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def helperLiCreateTree(li):
    # 判断arr是否为空
    if len(li) == 0:
        return TreeNode(li[0])
    mid = len(li) // 2  # 有序数组的中间元素的下标

    if len(li) > 0:
        # 将中间元素作为二叉树的根
        root = TreeNode(li[mid])
        # 如果左边的元素个数不为零，则递归调用函数，生成左子树
        if len(li[:mid]) > 0:
            root.left = helperLiCreateTree(li[:mid])
        # 如果右边的元素个数不为零，则递归调用函数，生成左子树
        if len(li[mid + 1:]) > 0:
            root.right = helperLiCreateTree(li[mid + 1:])
    return root


def helperPrintLinkListVal(head):
    if not head:
        print('链表是空的')
        return

    while head:
        print(head.val, end='->')
        head = head.next
    print()
