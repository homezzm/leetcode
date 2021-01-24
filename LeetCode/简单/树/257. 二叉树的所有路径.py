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
        给定一个二叉树，返回所有从根节点到叶子节点的路径。
        说明: 叶子节点是指没有子节点的节点。
        """
        res = []

        def dfs(node, path):
            if not node: return

            if not node.left and not node.right:
                path += str(node.val)
                res.append(path)

            path += str(node.val) + "->"

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root,'')
        return res


if __name__ == '__main__':
    genBiTreeByList = GenBiTreeByList()
    root = genBiTreeByList.gen_btree_by_list_1([1, 2, 3, None, 5])

    solution = Solution()
    print(solution.binaryTreePaths(root))
