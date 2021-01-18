# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from LeetCode.GenBTreeByList import *

class Solution(object):
    """
    https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/
    """
    def levelOrderBottom(self, root):
        if not root: return []
        queue = deque([root])
        li = []
        while queue:
            levels = []
            for _ in range(len(queue)):
                node = queue.popleft()
                levels.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            li.append(levels)
        return li[::-1]


if __name__ == '__main__':
    genBiTreeByList = GenBiTreeByList()
    root = genBiTreeByList.gen_btree_by_list_1([1,2,3,4,None,None,5])

    solution = Solution()
    print(solution.levelOrderBottom(root))