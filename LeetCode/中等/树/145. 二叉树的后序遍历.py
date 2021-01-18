# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def postorderTraversal(self, root):
        """
        https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
        :type root: TreeNode
        :rtype: List[int]
        不让用递归
        """
        if not root: return []
        stack, res = [], []
        stack.append(root)
        while len(stack)>0:
            node = stack.pop()
            if node:
                stack.append(node)
                stack.append(None)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            else:
                node = stack.pop()
                res.append(node.val)
        return res
