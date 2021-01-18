# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        https://leetcode-cn.com/problems/convert-bst-to-greater-tree/
        :type root: TreeNode
        :rtype: TreeNode
        你仔细看这棵树，他是中序给倒过来了，右中左这么遍历，然后每个节点的值进行累加的
        """
        sumVal = 0
        # 下面是迭代
        if not root: return root
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if node:
                if node.left:
                    stack.append(node.left)
                stack.append(node)
                stack.append(None)
                if node.right:
                    stack.append(node.right)
            else:
                node = stack.pop()
                sumVal += node.val
                node.val = sumVal

        # 下面是递归
        # def inOrder(node):
        #     nonlocal sumVal
        #     if not node: return
        #     inOrder(node.right)
        #
        #     sumVal += node.val
        #     node.val = sumVal
        #
        #     inOrder(node.left)
        # inOrder(root)

        return root
