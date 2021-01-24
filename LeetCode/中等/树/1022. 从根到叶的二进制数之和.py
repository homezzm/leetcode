# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumRootToLeaf(self, root):
        """
        https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers/
        :type root: TreeNode
        :rtype: int
        给出一棵二叉树，其上每个结点的值都是0或1。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。
        例如，如果路径为0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数01101，也就是13。
        对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。
        返回这些数字之和。题目数据保证答案是一个 32 位 整数。

        101=
        1*2^0=1
        1*2+0*2^0=2
        2*2+1*2^0=5
        """
        if not root: return 0
        ans = 0

        def dfs(node, sumVal):
            if not node: return

            sumVal = sumVal * 2 + node.val

            if not node.left and not node.right:  # 到了叶子节点
                nonlocal ans
                ans += sumVal
            dfs(node.left, sumVal)
            dfs(node.right, sumVal)

        dfs(root, 0)
        return ans


if __name__ == '__main__':
    root = TreeNode(val=1, left=TreeNode(val=0, left=TreeNode(val=0, left=None, right=None),
                                         right=TreeNode(val=1, left=None, right=None)),
                    right=TreeNode(val=1, left=TreeNode(val=0, left=None, right=None),
                                   right=TreeNode(val=1, left=None, right=None)))
    solution = Solution()
    print(solution.sumRootToLeaf(root))
