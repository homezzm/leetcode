# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []

        # def dfs(node, li):
        #     #if not node: return
        #
        #     if not node:
        #         return
        #     if not node.left and not node.right:
        #         res.append([i for i in li])
        #         return
        #
        #     li.append(node.val)
        #
        #     dfs(node.left, li)
        #     dfs(node.right, li)
        #     li.pop()
        #
        # dfs(root, [])
        # return res

        # def f(r, s):
        #     if r:
        #         s = s * 2 + r.val
        #         if not r.left and not r.right:
        #             return s
        #         return f(r.left, s) + f(r.right, s)
        #     return 0
        #
        # return f(root, 0)


if __name__ == '__main__':
    root = TreeNode(val=1, left=TreeNode(val=0, left=TreeNode(val=0, left=None, right=None),
                                         right=TreeNode(val=1, left=None, right=None)),
                    right=TreeNode(val=1, left=TreeNode(val=0, left=None, right=None),
                                   right=TreeNode(val=1, left=None, right=None)))
    solution = Solution()
    print(solution.sumRootToLeaf(root))
