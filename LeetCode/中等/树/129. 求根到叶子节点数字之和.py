# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumNumbers(self, root):
        """
        https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/
        :type root: TreeNode
        :rtype: int
        """
        res = 0

        def dfs(node, sumVal):
            nonlocal res
            if not node:  return
            sumVal = sumVal * 10 + node.val
            if not node.left and not node.right:
                res += sumVal
            dfs(node.left, sumVal)
            dfs(node.right, sumVal)

        dfs(root, 0)
        return res

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if not root:return False
        def dfs(node, sumVal):
            if not node: return False
            sumVal += node.val
            if not node.left and not node.right:
                return sumVal == sum

            return dfs(node.left, sumVal) or dfs(node.right, sumVal)

        return dfs(root, 0)


if __name__ == '__main__':
    solution = Solution()
    # root = TreeNode(val=4, left=TreeNode(val=9, left=TreeNode(val=5, left=None, right=None),
    #                                      right=TreeNode(val=1, left=None, right=None)),
    #                 right=TreeNode(val=0, left=None, right=None))
    # print(solution.sumNumbers(root))
    root = TreeNode(val= 1, left= TreeNode(val= 2, left= None, right= None), right= None)


    print(solution.hasPathSum(root, 2))
