# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from LeetCode.GenBTreeByList import GenBiTreeByList


class Solution(object):

    def sumOfLeftLeaves(self, root):
        """
        https://leetcode-cn.com/problems/sum-of-left-leaves/
        :type root: TreeNode
        :rtype: int
        thinking:使用递归进行深度优先搜索
        1终止条件=没有左右子节点
        2返回值=叶子节点的值
        3子问题=必须是左节点
        """
        isLeafNode = lambda node: not node.left and not node.right

        def dfs(node):
            ans = 0
            if node.left:
                if isLeafNode(node.left):
                    ans += node.left.val
                else:
                    ans += dfs(node.left)
            if node.right and not isLeafNode(node.right):
                ans += dfs(node.right)
            return ans

        return dfs(root) if root else 0


if __name__ == '__main__':
    genBiTreeByList = GenBiTreeByList()
    root = genBiTreeByList.gen_btree_by_list_1([1, 2, 3, 4, 5])

    solution = Solution()
    print(solution.sumOfLeftLeaves(root))
