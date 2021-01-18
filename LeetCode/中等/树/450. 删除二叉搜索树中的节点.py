# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def deleteNode(self, root, key):
        """
        https://leetcode-cn.com/problems/delete-node-in-a-bst/
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:  # 当前节点既有左子树又有右子树
                tmp = root.right
                while tmp.left:
                    tmp = tmp.left
                tmp.left = root.left #将root的左子树放到root的右子树的最下面的左叶子节点的左子树上
                return root.right

        return root


if __name__ == '__main__':
    root = TreeNode(val=5, left=TreeNode(val=3, left=None, right=None), right=TreeNode(val=6, left=None, right=None))

    solution = Solution()
    solution.deleteNode(root, 0)
