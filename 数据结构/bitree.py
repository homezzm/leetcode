from collections import deque


# 二叉树遍历
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None  # 左孩子
        self.right = None  # 右孩子


a = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')
f = TreeNode('F')
g = TreeNode('G')

# 把节点都关联起来
e.left = a
e.right = g
a.right = c
c.left = b
c.right = d
g.right = f

root = e

print('----------------------前序遍历----------------------')


def pre_order(root):
    """前序遍历 根,左,右"""
    if root:  # 如果不为空（递归条件）
        print(root.val, end=',')  # 处理根节点
        pre_order(root.left)  # 递归左子树
        pre_order(root.right)  # 递归右子树


pre_order(root)  # E,A,C,B,D,G,F,

print('\n', '----------------------中序遍历----------------------')


def in_order(root):
    """中序遍历 左，根，右"""
    if root:
        in_order(root.left)  # 递归左子树
        print(root.val, end=',')  # 处理根节点
        in_order(root.right)  # 递归右子树


in_order(root)  # A,B,C,D,E,G,F,　

print('\n', '----------------------后序遍历----------------------')


def post_order(root):
    """后序遍历 左，右，后"""
    if root:
        post_order(root.left)  # 递归左子树
        post_order(root.right)  # 递归右子树
        print(root.val, end=",")  # 处理根节点


post_order(root)  # B,D,C,A,F,G,E,

print('\n', '----------------------层次遍历----------------------')

def level_order(root):
    """层次遍历，节点一层一层入栈"""
    queue = deque()
    queue.append(root)
    while queue:
        n = len(queue)
        for _ in range(n):  # 每一次循环就是二叉树的一层节点
            node = queue.popleft()
            print(node.val, end=',')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def level_order(root):
    """层次遍历"""
    queue = deque()
    queue.append(root)
    while len(queue) > 0:  # 只要队不空
        node = queue.popleft()  # 出队
        print(node.val, end=',')
        if node.left:  # 有左孩子进队
            queue.append(node.left)
        if node.right:  # 有右孩子进队
            queue.append(node.right)


level_order(root)  # E,A,G,C,F,B,D,

print('\n', '----------------------迭代方法只有中间那段在变换----------------------')
print('\n', '----------------------迭代方法，使用栈前序遍历----------------------')


def preOrderTraversal(root):
    """前序遍历 根,左,右"""
    stack = []
    if root: stack.append(root)
    while len(stack) > 0:
        node = stack.pop()
        if node:
            if node.right: stack.append(node.right)  # 右 模拟栈的顺序
            if node.left: stack.append(node.left)  # 左

            stack.append(node)  # 根
            stack.append(None)
        else:
            node = stack.pop()
            print(node.data, end=',')


preOrderTraversal(root)  # E,A,C,B,D,G,F,

print('\n', '----------------------迭代方法，使用栈中序遍历----------------------')


def inOrderTraversal(root):
    """中序遍历 左，根，右"""
    stack = []
    if root: stack.append(root)
    while len(stack) > 0:
        node = stack.pop()  # 拿到栈顶节点
        if node:
            if node.right:
                stack.append(node.right)  # 添加右节点（空节点不入栈）

            stack.append(node)
            # 要处理的节点放入栈之后，紧接着放入一个空指针作为标记，中序遍历，根节点即为要处理的节点
            stack.append(None)  # 中节点访问过，但是还没有处理，加入空节点做为标记。

            if node.left:
                stack.append(node.left)  # 添加左节点（空节点不入栈）

        else:  # 只有遇到空节点的时候，才将下一个节点放进结果集
            node = stack.pop()  # 重新取出栈中元素
            print(node.data, end=',')  # 处理节点


inOrderTraversal(root)  # A,B,C,D,E,G,F,　

print('\n', '----------------------迭代方法，使用栈后序遍历----------------------')


def postOrderTraversal(root):
    """后序遍历 左，右，根"""
    stack = []
    if root: stack.append(root)
    while len(stack) > 0:
        node = stack.pop()  # 拿到栈顶节点
        if node:
            stack.append(node)
            # 要处理的节点放入栈之后，紧接着放入一个空指针作为标记，中序遍历，根节点即为要处理的节点
            stack.append(None)  # 中节点访问过，但是还没有处理，加入空节点做为标记。
            if node.right:
                stack.append(node.right)  # 添加右节点（空节点不入栈）
            if node.left:
                stack.append(node.left)  # 添加左节点（空节点不入栈）

        else:  # 只有遇到空节点的时候，才将下一个节点放进结果集
            node = stack.pop()  # 重新取出栈中元素
            print(node.data, end=',')  # 处理节点


postOrderTraversal(root)  # B,D,C,A,F,G,E,
