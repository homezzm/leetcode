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
        https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/
        :type root: TreeNode
        :rtype: List[int]
        从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
        层次遍历
        """
        res = []
        if not root: return res
        q = deque()
        q.append(root)
        while q:
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                res.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
