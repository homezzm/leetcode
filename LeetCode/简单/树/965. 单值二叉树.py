# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from LeetCode.GenBTreeByList import GenBiTreeByList


class Solution(object):
    def isUnivalTree(self, root):
        """
        https://leetcode-cn.com/problems/univalued-binary-tree/
        :type root: TreeNode
        :rtype: bool
        """
        dicts = {}
        self.isUnivalTreeRecursion(root, dicts)
        return True if len(dicts) == 1 else False

    def isUnivalTreeRecursion(self, root, dicts):
        if not root: return dicts
        dicts[root.val] = root.val
        self.isUnivalTreeRecursion(root.left, dicts)
        self.isUnivalTreeRecursion(root.right, dicts)


if __name__ == '__main__':
    genBiTreeByList = GenBiTreeByList()
    root = genBiTreeByList.gen_btree_by_list_1([1,1,1,1,1,None,1])

    solution = Solution()
    print(solution.isUnivalTree(root))
