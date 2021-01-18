# 根据列表生成一个棵二叉树，做题用
class BiTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None  # 左孩子
        self.right = None  # 右孩子


class GenBiTreeByList:
    def gen_btree_by_list(self, root, li, inx):
        for i in range(0, len(li)):
            left = 2 * inx + 1
            right = 2 * inx + 2

            n = len(li)
            if left > n or right > n: return

            if  li[left]:
                root.left = BiTreeNode(li[left])
                self.gen_btree_by_list(root.left, li, left)
            if  li[right]:
                root.right = BiTreeNode(li[right])
                self.gen_btree_by_list(root.right, li, right)


    def gen_btree_by_list_1(self, li):
        root = BiTreeNode(li[0])
        self.gen_btree_by_list(root, li, 0)
        return root


if __name__ == '__main__':
    gen = GenBiTreeByList();
    root = gen.gen_btree_by_list_1([1, 2, 2, 3, 4, 4, 3])
    print(root)
