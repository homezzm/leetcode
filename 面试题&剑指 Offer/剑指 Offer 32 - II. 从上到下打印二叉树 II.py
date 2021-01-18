# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root: return res
        q = deque()
        q.append(root)
        while q:
            length = len(q)
            li = []
            for _ in range(length):
                node = q.popleft()
                li.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(li)
        return res
