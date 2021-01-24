# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        https://leetcode-cn.com/problems/balanced-binary-tree/
        :type root: TreeNode
        :rtype: bool
        给定一个二叉树，判断它是否是高度平衡的二叉树。
        本题中，一棵高度平衡二叉树定义为：
        一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
        """
        if not root: return True
        #左右要都是平衡二叉树，且左右高度绝对值不超过 1
        return self.isBalanced(root.left) and self.isBalanced(root.right) and \
               abs(self.depth(root.left) - self.depth(root.right)) <= 1

    def depth(self, root):
        if not root: return 0
        #求左右树最大深度，别忘了加上根+1
        return max(self.depth(root.left), self.depth(root.right)) + 1

        # if not root: return True
        #
        # def dfs(node):
        #     if not node: return 0
        #     left = dfs(node.left)
        #     if left == -1: return -1
        #     right = dfs(node.right)
        #     if right == -1: return -1
        #
        #     return max(left, right) + 1 if abs(left - right) < 2 else -1
        #
        # return dfs(root) != -1
