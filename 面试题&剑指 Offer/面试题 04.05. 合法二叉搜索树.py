# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        https://leetcode-cn.com/problems/legal-binary-search-tree-lcci/
        :type root: TreeNode
        :rtype: bool
        实现一个函数，检查一棵二叉树是否为二叉搜索树。
        thinking:深度优先 前序遍历 根左右
        终止条件：已越过叶子节点 返回True
        子问题：True if 左孩子<当前节点<右孩子 else False
        """
        # 判断中序遍历是否是递增的

        if not root: return True
        pre, flag = float('-inf'), True

        def inOrder(node):
            nonlocal pre, flag
            if not node or not flag: return
            inOrder(node.left)

            if pre < node.val:
                pre = node.val
            else:
                flag = False

            inOrder(node.right)

        inOrder(root)
        return flag

        # def dfs(node, minVal, maxVal):
        #     if not node: return True
        #     #10>=
        #     if node.val >= maxVal or node.val <= minVal: return False
        #     return dfs(root.left, minVal, node.val) and dfs(root.right, root.val, maxVal)

        # return dfs(root, float('-inf'), float('inf'))

        # if not root: return True
        #
        # def dfs(node):
        #     if not node: return True
        #
        #     if node.left and node.left.val >= node.val:
        #         return False
        #     if node.right and node.right.val <= node.val:
        #         return False
        #     return dfs(node.left) and dfs(node.right)
        #
        # return dfs(root)
