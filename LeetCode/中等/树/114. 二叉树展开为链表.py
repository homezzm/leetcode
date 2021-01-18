# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        """
        https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root: return

        preNode = None

        def preOrder(node):
            nonlocal preNode
            if not node: return
            preOrder(node.right)
            preOrder(node.left)

            node.right = preNode
            node.left = None
            preNode = node
        #变成6,5,4,3,2,1这的顺序，然后倒着改变每一个节点的right即可

        preOrder(root)


if __name__ == '__main__':
    root = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=3, left=None, right=None),
                                         right=TreeNode(val=4, left=None, right=None)),
                    right=TreeNode(val=5, left=None, right=TreeNode(val=6, left=None, right=None)))

    solution = Solution()
    solution.flatten(root)
