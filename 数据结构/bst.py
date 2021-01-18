# 二叉搜索树

class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子
        self.parent = None  # 父节点


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    def insert(self, node, val):
        """
        插入函数，使用递归
        :param node: 要插入到哪个节点下
        :param val: 要插入的值
        :return:
        """
        if not node:  # 节点是空的情况
            # 找到这个节点了，直接插入即可
            # 这里创建了一个节点，但还没有与树进行关联
            node = BiTreeNode(val)
        elif val < node.val:
            # 往左走，递归调用左孩子
            node.left = self.insert(node.left, val)
            # 连上左孩子的父节点
            node.left.parent = node
        elif val > node.val:
            # 往右走，递归调用右孩子
            node.right = self.insert(node.right, val)
            # 连上右孩子的父节点
            node.right.parent = node
            # 其实还有一种情况就是 值等于某个叶子节点，理论上是不允许有重复值的
            # 这种情况的一种解决办法是，找到相同值的叶子节点，增加一个count属性
        return node

    def insert_no_rec(self, val):
        """
        插入函数，不使用递归
        :param node: 要插入到哪个节点下
        :param val: 要插入的值
        :return:
        """
        p = self.root
        if not p:  # 节点是空的情况下
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:  # 如果左孩子存在
                    p = p.lchild
                else:  # 左孩子不存在
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
                    return
            elif val > p.data:
                if p.rchild:  # 如果右孩子存在
                    p = p.rchild
                else:  # 右孩子不存在
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:  # 等于的情况直接返回
                return

    def query(self, node, val):
        """
        查询也是有递归版本与非递归版本的，递归版本都要带node参数
        :param node:
        :param val:
        :return:
        """
        if not node:  # 节点为空
            return None
        if node.val < val:  # 找右边
            return self.query(node.right, val)
        elif node.val > val:  # 找左边
            return self.query(node.left, val)
        else:  # 等于
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.val < val:  # 找右边
                p = p.right
            elif p.val > val:  # 找左边
                p = p.left
            else:
                return p
        return None

    def pre_order(self, root):
        """前序遍历 根,左,右"""
        if root:  # 如果不为空（递归条件）
            print(root.val, end=',')  # 访问自己
            self.pre_order(root.left)  # 递归左子树
            self.pre_order(root.right)  # 递归右子树

    def in_order(self, root):
        """中序遍历 左，根，右"""
        if root:
            self.in_order(root.left)  # 递归左子树
            print(root.val, end=',')  # 访问自己
            self.in_order(root.right)  # 递归右子树

    def post_order(self, root):
        """后序遍历 左，右，后"""
        if root:
            self.post_order(root.left)  # 递归左子树
            self.post_order(root.right)  # 递归右子树
            print(root.val, end=",")  # 访问自己

    def __remove_node_1(self, node):
        # 情况1：node是叶子节点，就是没有孩子
        # 如果参数node的parent是空那它就是父节点
        # 只有根的parent是none，如果是根节点，直接赋值None即可
        if not node.parent:
            self.root = None
        # 如果不是根节点，就把参数node与它父亲断绝关系
        if node == node.parent.left:
            # 如果参数node是他父亲的左孩子
            node.parent.left = None
        else:
            # 如果参数node是他父亲的右孩子
            node.parent.right = None

    def __remove_node_21(self, node):
        # 情况2.1：node只有一个左孩子
        if not node.parent:
            # 如果参数node是根节点，那删除后，它的左孩子就成为新的根了
            self.root = node.left
            # 左孩子成为了根，他就没爹了
            node.left.parent = None
        elif node == node.parent.left:
            # 如果参数node是他父亲的左孩子
            node.parent.left = node.left
            # 把参数node的左孩子连到node原来的parent上
            node.left.parent = node.parent
        else:
            # 如果参数node是他父亲的右孩子
            node.parent.right = node.left
            node.left.parent = node.parent

    def __remove_node_22(self, node):
        # 情况2.2：node只有一个右孩子
        if not node.parent:
            # 如果参数node是根节点，那删除后，它的右孩子就成为新的根了
            self.root = node.right
            # 右孩子成为了根，他就没爹了
            node.right.parent = None
        elif node == node.parent.left:
            # 如果参数node是他父亲的左孩子
            node.parent.left = node.right
            # 把参数node的左孩子连到node原来的parent上
            node.left.parent = node.parent
        else:
            # 如果参数node是他父亲的右孩子
            node.parent.right = node.right
            node.right.parent = node.parent

    def delete(self, val):
        if self.root:  # 不是空树在删除
            # 删除前要先找到这个节点
            node = self.query_no_rec(val)
            if not node:  # 这节点不存在
                return False
            # 接下来就是三种情况
            if not node.lchild and not node.rchild:
                # 情况1 是叶子节点，没孩子
                self.__remove_node_1(node)
            elif not node.rchild:
                # 情况2.1 如果没有右孩子，那它一定有左孩子
                self.__remove_node_21(node)
            elif not node.lchild:
                # 情况2.2 如果没有左孩子，那它一定有右孩子
                self.__remove_node_22(node)
            else:
                # 情况3 有两孩子
                # 先找右子树里最小的节点
                min_node = node.rchild
                while min_node.left:
                    # 有左孩子我就一直往左走
                    min_node = min_node.left
                # 找到右子树里最小节点后，开始进行替换
                node.data = min_node.val
                # 在删除min_node 该节点要么没孩子，要么只有一个右孩子，因为他本身就是左边最小的了
                if min_node.right:  # 如果有右孩子
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)


if __name__ == '__main__':
    tree = BST([1, 4, 2, 5, 3, 8, 6, 9, 7])
    tree.in_order(tree.root)
    print('')

    tree.delete(4)
    tree.delete(1)
    tree.in_order(tree.root)

    # tree = BST([4, 6, 7, 9, 2, 1, 3, 5, 8])
    # # print(tree.query_no_rec(5).val)
    # tree.pre_order(tree.root)
    # print('')
    # tree.in_order(tree.root)
    # print('')
    # tree.post_order(tree.root)
