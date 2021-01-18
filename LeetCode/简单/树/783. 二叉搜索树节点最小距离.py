# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys

from LeetCode.GenBTreeByList import GenBiTreeByList
from LeetCode.Helpers import helperLiCreateTree


class Solution(object):
    def minDiffInBST(self, root):
        """
        https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/
        :type root: TreeNode
        :rtype: int
        在二叉搜索树中，中序遍历会将树中节点按数值大小顺序输出。只需要遍历计算相邻数的差值，取其中最小的就可以了。
        """
        pre, ans = None, sys.maxsize

        def dfs(node):
            nonlocal pre, ans
            if not node: return
            dfs(node.left)
            if pre:
                ans = min(ans, node.val - pre.val)
            pre = node

            dfs(node.right)

        dfs(root)
        return ans


if __name__ == '__main__':
    genBiTreeByList = GenBiTreeByList()
    root = genBiTreeByList.gen_btree_by_list_1([4, 2, 6, 1, 3, None, None])

    solution = Solution()
    print(solution.minDiffInBST(root))
