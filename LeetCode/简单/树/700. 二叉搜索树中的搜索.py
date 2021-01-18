# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution(object):
    def searchBST(self, root, val):
        """
        https://leetcode-cn.com/problems/search-in-a-binary-search-tree/
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # if not root or root.val == val: return root
        #
        # return self.searchBST(root.left, val) if val < root.val \
        #     else self.searchBST(root.right, val)

        # 迭代更牛的方法，官方的
        # 二叉搜索树是一棵二叉树，每个节点都有以下特性：大于左子树上任意一个节点的值
        # 小于右子树上任意一个节点的值
        while root and val != root.val:
            root = root.left if val < root.val else root.right
        return root

        # 下面是层次遍历
        # if not root or root.val == val: return root
        # q = deque()
        # q.append(root)
        # while q:
        #     node = q.popleft()
        #     if node.val == val:
        #         return node
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        # return None
