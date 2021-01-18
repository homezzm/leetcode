class Solution(object):
    def sortedSquares(self, nums):
        """
        https://leetcode-cn.com/problems/squares-of-a-sorted-array/
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1
        resultCount = right
        while left <= right:
            if nums[left] * nums[left] < nums[right] * nums[right]:
                result[resultCount] = nums[right] * nums[right]
                right -= 1
            else:
                result[resultCount] = nums[left] * nums[left]
                left += 1

            resultCount -= 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortedSquares([-4, -1, 0, 3, 10]))
