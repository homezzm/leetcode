class Solution(object):
    def missingNumber(self, nums):
        """
        https://leetcode-cn.com/problems/missing-number/
        :type nums: List[int]
        :rtype: int
        """
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


if __name__ == '__main__':
    solution = Solution()
    print(solution.missingNumber([9,6,4,2,3,5,7,0,1]))
