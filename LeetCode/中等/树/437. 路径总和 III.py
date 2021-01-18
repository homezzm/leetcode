# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        https://leetcode-cn.com/problems/path-sum-iii/
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root: return 0

        def dfs(node, sumVal):
            if not node: return 0
            sumVal -= node.val
            res = 1 if sumVal == 0 else 0  # 如果当前sum为0就说明找到一条路径 res+1
            return res + dfs(node.left, sumVal) + dfs(node.right, sumVal)

        result = dfs(root, sum)
        left = self.pathSum(root.left, sum)
        right = self.pathSum(root.right, sum)
        return result + left + right


if __name__ == '__main__':
    li = [1, 2, 3]
    for i in li[:-1]:
        print(i)
    # print(sum(li) == 1)
