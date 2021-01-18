# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def findTarget(self, root, k):
        """
        https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/
        :type root: TreeNode
        :type k: int
        :rtype: bool
        层次变量，看队列中的元素是否有两个元素，如果有，则看两个元素是否与k相同
        相同则返回true，不同继续比较
        """
        if not root: return False

        q, li = deque(), []
        q.append(root)
        while len(q) > 0:
            node = q.popleft()
            if k - node.val in li: return True
            else: li.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False
