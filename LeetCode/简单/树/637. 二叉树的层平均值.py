# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

from LeetCode.GenBTreeByList import GenBiTreeByList


class Solution(object):
    def averageOfLevels(self, root):
        """
        https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/
        :type root: TreeNode
        :rtype: List[float]
        层次遍历？
        """
        if not root: return []
        li, q = [], deque()
        q.append(root)
        while q:
            total, size = 0, len(q)
            for _ in range(size):
                node = q.popleft()
                total += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            li.append(total / size)
        return li


if __name__ == '__main__':
    genBiTreeByList = GenBiTreeByList()
    root = genBiTreeByList.gen_btree_by_list_1([3, 9, 20, 15, 7])

    solution = Solution()
    print(solution.averageOfLevels(root))
