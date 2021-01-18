from LeetCode.GenBTreeByList import *


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    """
    https://leetcode-cn.com/problems/symmetric-tree/
    """
    def isSymmetric(self, root):
        self.isSymmetricRecursion(root, root)

    def isSymmetricRecursion(self, tree1, tree2):
        if not tree1 and not tree2: return True  # 两树都空
        if not tree1 or not tree2: return False  # 有一棵空

        return tree1.val == tree2.val \
               and self.isSymmetricRecursion(tree1.right, tree2.left) \
               and self.isSymmetricRecursion(tree1.left, tree2.right)


if __name__ == '__main__':
    genBiTreeByList = GenBiTreeByList()
    root = genBiTreeByList.gen_btree_by_list_1([1, 2, 2, 3, 4, 4, 3])

    solution = Solution()
    print(solution.isSymmetric(root))
