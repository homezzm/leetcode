# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        https://leetcode-cn.com/problems/maximum-binary-tree/
        :type nums: List[int]
        :rtype: TreeNode
        """

        def generateTree(li):
            if len(li) == 0: return None
            maxVal = max(li)  # 找到最大值
            maxValInx = li.index(maxVal)  # 最大值左边是左子树，右边是右子树

            root = TreeNode(maxVal)
            root.left = generateTree(li[0:maxValInx])
            root.right = generateTree(li[maxValInx + 1:])

            return root
        return generateTree(nums)


if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    print(nums[4:])
