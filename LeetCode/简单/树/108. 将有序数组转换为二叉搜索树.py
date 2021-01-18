# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
        :type nums: List[int]
        :rtype: TreeNode
        左子树小于根，右子树大于根，
        对于生成树来主说最主要的就是确定根节点，由是nums是已经排好序的，所以取中间值即
        中序遍历也会生成排好序的列表
        """

        def arrayToBst(arr, left, right):
            if left == right: return None  # 指针对撞了，就结束了

            mid = (left + right) // 2  # 确定根节点
            root = TreeNode(nums[mid])
            root.left = arrayToBst(arr, left, mid)  # 二分了就
            root.right = arrayToBst(arr, mid + 1, right)
            return root
        return arrayToBst(nums,0,len(nums))

if __name__ == '__main__':
    solution=Solution   ()
    print(solution.sortedArrayToBST([-10,-3,0,5,9]))
