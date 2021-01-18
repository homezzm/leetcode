from 数据结构.bst import BiTreeNode, BST


class AVLNode(BiTreeNode):  # 结构大多相同，就直接继承了
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0  # 平衡因子，新创建的节点默认就是0


class AVLTree(BST):  # 大多操作方法都一样
    def __init__(self, li=None):
        BST.__init__(self, li)

    def rotate_left(self, p, c):
        # 左旋
        s2 = c.left
        p.right = s2
        if s2:
            s2.parent = p
        c.left = p
        p.parent = c
        # bf平衡因子是要随时更新的
        p.bf, c.bf = 0, 0
        return c

    def rotate_right(self, p, c):
        # 右旋
        s2 = c.right
        p.left = s2
        if s2:
            s2.parent = p
        c.right = p
        p.parent = c
        p.bf, c.bf = 0, 0
        return c

    def rotate_right_left(self, p, c):
        # 右左旋
        g = c.left

        s3 = g.right
        c.left = s3

        if s3:
            s3.parent = c
        g.right = c
        c.parent = g

        # 上面是右旋，下面是左旋
        s2 = g.left  # 左孩子
        p.right = s2
        if s2:
            s2.parent = p
        g.left = p
        p.parent = g
        # bf平衡因子是要随时更新的

    def insert_no_rec(self, val):
        pass
