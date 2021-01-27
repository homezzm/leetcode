class Solution(object):
    def subsets(self, nums):
        """
        https://leetcode-cn.com/problems/subsets/
        :type nums: List[int]
        :rtype: List[List[int]]
        给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
        解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
        输入：nums = [1,2,3] 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        输入：nums = [0] 输出：[[],[0]]
        """
        res = []
        #对res的更新 使用了 前序遍历
        def backtrack(start, tracks):
            res.append(tracks[:])

            for i in range(start, len(nums)):
                tracks.append(nums[i])
                backtrack(i + 1, tracks)
                tracks.pop()

        backtrack(0, [])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2, 3]))
