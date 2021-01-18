# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        https://leetcode-cn.com/problems/range-sum-of-bst/
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        层次遍历，找出low<=val>=high  7<= 8 <=10
        找出后放到li中
        """
        # if not root: return 0
        # res = lambda val: low <= val <= high
        # li = []
        #
        # def dfs(node):
        #     if not node: return
        #     if res(node.val): li.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)
        #
        # dfs(root)
        # return sum(li)

        # 以下是迭代
        if not root: return 0
        res = lambda val: low <= val <= high
        q, ans = deque(), 0
        q.append(root)

        while q:
            node = q.popleft()
            if res(node.val): ans += node.val
            if low < node.val: q.append(node.left)
            if node.val < high: q.append(node.right)
        return ans

        # if not root: return 0
        # res = lambda val: low <= val <= high
        # q, li = deque(), []
        # q.append(root)
        #
        # while q:
        #     node = q.popleft()
        #     if res(node.val): li.append(node.val)
        #     if node.left: q.append(node.left)
        #     if node.right: q.append(node.right)
        # return sum(li)
