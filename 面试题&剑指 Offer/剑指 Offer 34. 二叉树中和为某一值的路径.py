# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root, sum):
        """
        https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
        给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
        返回：[[5,4,11,2],[5,8,4,5]]
        """

        res, path = [], []

        def dfs(node, sumVal):
            if not node: return
            path.append(node.val)
            sumVal -= node.val
            if sumVal == 0 and not node.left and not node.right:
                res.append(path[:])

            dfs(node.left, sumVal)
            dfs(node.right, sumVal)
            path.pop()  # 回溯一下

        dfs(root, sum)
        return res


if __name__ == '__main__':
    root = TreeNode(val=-2, left=None, right=TreeNode(val=-3, left=None, right=None))

    solution = Solution()
    print(solution.pathSum(root, -5))
