# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preorderTraversal(self, root):
        """
        https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
        :type root: TreeNode
        :rtype: List[int]
        """ 
        if not root: return
        stack, li = [root], []
        while len(stack) > 0:
            node = stack.pop()
            if node:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                stack.append(node)
                stack.append(None)
            else:
                node = stack.pop()
                li.append(node.val)
        return li

        # 递归实现
        # li = []
        #
        # def preOrder(node):
        #     if not node: return
        #     li.append(node.val)
        #     preOrder(node.left)
        #     preOrder(node.right)
        # preOrder(root)
        # return li
if __name__ == '__main__':
    root= TreeNode(val= 1, left= None, right= TreeNode(val= 2, left= TreeNode(val= 3, left= None, right= None), right= None))

    solution=Solution()
    print(solution.preorderTraversal(root))