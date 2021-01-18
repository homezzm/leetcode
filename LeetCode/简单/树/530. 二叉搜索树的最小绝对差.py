# Definition for a binary tree node.
import sys

from LeetCode.GenBTreeByList import GenBiTreeByList


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getMinimumDifference(self, root):
        """
        https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
        :type root: TreeNode
        :rtype: int
        """
        cur, ans, pre, stack = root, float('inf'), -1, []
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre != -1:
                    ans = min(ans, cur.val - pre)
                pre = cur.val
                cur = cur.right
        return ans

        #递归方式
        # pre, minVal = None, sys.maxsize  # 前一个节点
        #
        # def inOrder(node):
        #     nonlocal pre, minVal
        #     if not node: return
        #
        #     inOrder(node.left)
        #
        #     if pre:
        #         minVal = min(minVal, node.val - pre.val)
        #
        #     pre = node
        #     inOrder(node.right)
        #
        # inOrder(root)
        # return minVal

if __name__ == '__main__':
    genBiTreeByList = GenBiTreeByList()
    root = genBiTreeByList.gen_btree_by_list_1([1,None,3,2])

    solution = Solution()
    print(solution.getMinimumDifference(root))