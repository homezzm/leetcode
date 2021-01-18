# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal/
        :type preorder: List[int]
        :rtype: TreeNode
        根据前序生成中序列，因为二叉搜索树的中序是有序的，把前序排一下序就可以了
        """
        inorder = sorted(preorder)
        def generateBinarySearchTree(pOrder, iOrder):
            if len(pOrder) == 0: return None
            root = TreeNode(pOrder[0])  # 根
            rootInx = iOrder.index(root.val)

            root.left = generateBinarySearchTree(pOrder[1:rootInx + 1], iOrder[0:rootInx + 1])
            root.right = generateBinarySearchTree(pOrder[rootInx+1:], iOrder[rootInx+1:])
            return root

        return generateBinarySearchTree(preorder,inorder)

print([1,2,3][1:])