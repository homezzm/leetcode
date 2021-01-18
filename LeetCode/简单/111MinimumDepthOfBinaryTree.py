# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from LeetCode.GenBTreeByList import GenBiTreeByList


class Solution(object):
    """
    https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
    """
    def minDepth(self, root):
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        #如果左子树或右子树的深度不为0，即存在一个子树，那么当前子树的最小深度就是该子树的深度 + 1
        #如果左子树和右子树的深度都不为0，即左右子树都存在，那么当前子树的最小深度就是它们较小值 + 1
        if not left or not right:
            return left + right + 1
        else:
            return min(left, right) + 1


if __name__ == '__main__':
    genBiTreeByList = GenBiTreeByList()
    root = genBiTreeByList.gen_btree_by_list_1([3,9,20,None,None,15,7])

    solution = Solution()
    print(solution.minDepth(root))
