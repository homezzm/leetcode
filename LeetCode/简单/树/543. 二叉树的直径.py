# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from LeetCode.GenBTreeByList import GenBiTreeByList


class Solution(object):
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root):
        """
        https://leetcode-cn.com/problems/diameter-of-binary-tree/
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.tree_recursion(root)
        return self.max_diameter

    def tree_recursion(self, root):
        left = 0 if not root.left else self.tree_recursion(root.left) + 1
        right = 0 if not root.right else self.tree_recursion(root.right) + 1
        self.max_diameter = max(self.max_diameter, left + right)
        return max(left, right)


if __name__ == '__main__':
    genBiTreeByList = GenBiTreeByList()
    root = genBiTreeByList.gen_btree_by_list_1([1, 2, 3, 4, 5])

    solution = Solution()
    print(solution.diameterOfBinaryTree(root))
