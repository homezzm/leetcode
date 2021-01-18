# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        前序 preorder = [1,2,4,7,3,5,6,8]
        中序 inorder = [4,7,2,1,5,3,8,6]
        后序 postorder = [7,4,2,5,8,6,3,1]
        只有前后序是推不出来二叉树的，必须有中序
        前序的第一个节点一定是根节点，后序的最后一个节点一定是根节点
        ------------------根据前序、中序生成二叉树---------------------
        1.前序第一个节点做为根
        2.在中序中找到前序第一个节点的位置，即1的位置，在中序中1的左边即为左子树[4,7,2]，1的右边即为右子树[5,3,8,6]。
        3.递归开始，还原左子树。前序中节点1找完了，找节点2.在中序中找到2的位置，2的左边即为2的左子树。
            1
           / \
          2  3
         /  / \
        4  5  6
        \     /
         7   8
        """
        #in[4, 7, 2, 1, 5, 3, 8, 6],
        #po[7, 4, 2, 5, 8, 6, 3, 1]
        def helper(iOrder, pOrder):
            if not pOrder: return None
            root = TreeNode(pOrder[-1])
            rootInx = iOrder.index(root.val) #3

            root.left = helper(iOrder[0:rootInx], pOrder[0:rootInx]) #in[4,7,2] po[7,4,2]
            root.right = helper(iOrder[rootInx + 1:], pOrder[rootInx:-1]) #in[5, 3, 8, 6] po[5, 8, 6, 3]
            return root

        return helper(inorder, postorder)


if __name__ == '__main__':
    solution = Solution()
    solution.buildTree([4, 7, 2, 1, 5, 3, 8, 6], [7, 4, 2, 5, 8, 6, 3, 1])
