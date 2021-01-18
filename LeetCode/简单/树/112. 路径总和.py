# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from LeetCode.GenBTreeByList import GenBiTreeByList


class Solution(object):
    """
    https://leetcode-cn.com/problems/path-sum/
    """

    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) \
               or self.hasPathSum(root.right, sum - root.val)


if __name__ == '__main__':
    genBiTreeByList = GenBiTreeByList()
    root = genBiTreeByList.gen_btree_by_list_1([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])

    solution = Solution()
    print(solution.hasPathSum(root, 22))
