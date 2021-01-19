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
        https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/
        :type root: TreeNode
        :rtype: List[List[int]]
        请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
        第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
        thinking:层次遍历，记录层次数，偶数层正序输出，奇数层倒序输出
        O(n) O(n2)
        也可以用双向对队来实现
        """

        if not root: return []
        q, odd, res = deque(), 0, []
        q.append(root)
        while q:
            length, li = len(q), []
            for _ in range(length):
                node = q.popleft()
                li.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if odd % 2 == 1:
                li.reverse()
            res.append(li)
            odd += 1
        return res
