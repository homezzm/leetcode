# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
https://leetcode-cn.com/problems/serialize-and-deserialize-bst/submissions/
二叉搜索树的特点是的中序序列是递增排序的序列inorder = sorted(preorder)，说明我们只需要知道了前序序列或后序序列相当于我们也知道了中序序列，可以通过排序获得。
"""


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        preOrderList = []

        def preOrder(node):
            if not node: return
            preOrderList.append(node.val)
            preOrder(node.left)
            preOrder(node.right)

        preOrder(root)
        return ' '.join(map(str, preOrderList))

    def deserialize(self, data):
        """Decodes your encoded val to tree.

        :type data: str
        :rtype: TreeNode
        根据传入的前序，生成中序，然后根据前中序生成二叉搜索树
        """
        if not data: return None
        li = data.replace('[', '').replace(']', '').replace(' ', '').split(',')
        preOrderList = li
        inOrderList = sorted(li)  # 获得中序
        return self.generateTree(preOrderList, inOrderList)

    def generateTree(self, preOrder, inOrder):
        if len(preOrder) == 0: return None
        root = TreeNode(preOrder[0])  # 前序第一个值为根
        rootInx = inOrder.index(root.val)  # 在中序中找到根的位置
        root.left = self.generateTree(preOrder[1:rootInx + 1], inOrder[0:rootInx])
        root.right = self.generateTree(preOrder[rootInx + 1:], inOrder[rootInx + 1:])
        return root


if __name__ == '__main__':
    # pre = [2, 1, 3]
    # ino = [1, 2, 3]
    # print(pre[1:2])
    root11 = TreeNode(val=2, left=TreeNode(val=1, left=None, right=None), right=TreeNode(val=3, left=None, right=None))
    ser = Codec()
    codec = Codec()
    ree = ser.serialize(root11)
    ans = codec.deserialize(ree)
    # print(ans.left.val)
