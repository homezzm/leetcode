# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from LeetCode.GenBTreeByList import GenBiTreeByList


class Solution(object):
    def binaryTreePaths(self, root):
        """
        https://leetcode-cn.com/problems/binary-tree-paths/
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, path, res):
        if not root: return

        if not root.left and not root.right:
            path += str(root.val)
            res.append(path)
            return res

        path += str(root.val) + "->"

        self.dfs(root.left, path, res)
        self.dfs(root.right, path, res)


if __name__ == '__main__':
    genBiTreeByList = GenBiTreeByList()
    root = genBiTreeByList.gen_btree_by_list_1([1, 2, 3, None, 5])

    solution = Solution()
    print(solution.binaryTreePaths(root))
