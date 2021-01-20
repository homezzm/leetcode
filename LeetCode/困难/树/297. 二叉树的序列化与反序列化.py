# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        preOrderList = []

        def preOrder(node):
            if not node:
                preOrderList.append('#')
                return
            preOrderList.append(node.val)
            preOrder(node.left)
            preOrder(node.right)

        preOrder(root)
        return ' '.join(map(str, preOrderList))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        preOrder = list(reversed(data.split(' ')))  # ['1', '2', '#', '#', '3', '4', '#', '#', '5', '#', '#']
        def generateBinaryTree(pre):
            if len(pre) == 0: return

            val = pre.pop()
            if val == '#':
                return None

            # 如果弹出的是数字，那就是做为根节点
            node = TreeNode(val)
            node.left = generateBinaryTree(pre)
            node.right = generateBinaryTree(pre)
            return node

        return generateBinaryTree(preOrder)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

if __name__ == '__main__':
    root = TreeNode(val=1, left=TreeNode(val=-2, left=None, right=None),
                    right=TreeNode(val=3, left=TreeNode(val=4, left=None, right=None),
                                   right=TreeNode(val=5, left=None, right=None)))

    # root = TreeNode(val=5, left=TreeNode(val=2, left=None, right=None),
    #                 right=TreeNode(val=4, left=TreeNode(val=3, left=None, right=None),
    #                                right=TreeNode(val=1, left=None, right=None)))
    codec = Codec()
    jsonstr = codec.serialize(root)
    print(codec.deserialize(jsonstr))
