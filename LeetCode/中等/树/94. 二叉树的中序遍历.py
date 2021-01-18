# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res = [root], []
        while len(stack) > 0:
            node = stack.pop()
            if node:
                if node.right: stack.append(node.right)
                stack.append(node)
                stack.append(None)
                if node.left: stack.append(node.left)
            else:
                node = stack.pop()
                res.append(node.val)
        return res

        # 递归实现
        # res = []
        #
        # def dfs(node):
        #     if node is None: return
        #     dfs(node.left)
        #     res.append(node.val)
        #     dfs(node.right)
        #
        # dfs(root)
        # return res
