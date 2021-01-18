class Solution(object):
    def rob(self, nums):
        """
        https://leetcode-cn.com/problems/house-robber/
        """
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            first, second = second, max(first + nums[i], second)

        return second


if __name__ == '__main__':
    solution = Solution()
    print(solution.rob([1,2,3]))
