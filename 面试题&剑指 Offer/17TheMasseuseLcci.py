class Solution(object):
    def massage(self, nums):
        """
        https://leetcode-cn.com/problems/the-masseuse-lcci/
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        if n == 1: return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            first, second = second, max(second, first + nums[i])
        return second


if __name__ == '__main__':
    solution = Solution()
    print(solution.massage([2, 7, 9, 3, 1]))


