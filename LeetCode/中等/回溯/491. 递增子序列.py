class Solution(object):
    def findSubsequences(self, nums):
        """
        https://leetcode-cn.com/problems/increasing-subsequences/
        :type nums: List[int]
        :rtype: List[List[int]]
        给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
        """

        res = []

        def backtrack(startInx, paths):
            if len(paths) > 1:
                res.append(paths[:])

            used = [0] * 201  # 题目范围为-100-100
            for i in range(startInx, len(nums)):
                if (len(paths) > 0 and nums[i] < paths[-1]) or used[nums[i] + 100] == 1:
                    continue

                used[nums[i] + 100] = 1  # 记录这个元素在本层⽤过了，本层后⾯不能再⽤了
                paths.append(nums[i])
                backtrack(i + 1, paths)
                paths.pop()

        backtrack(0, [])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.findSubsequences([4, 7, 6, 7]))
