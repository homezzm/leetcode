class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        https://leetcode-cn.com/problems/max-consecutive-ones/
        :type nums: List[int]
        :rtype: int
        thinking:1.暴力计数，遇0归0
        thinking:2.滑动窗口
        """

        # thinking:1遍历
        # if not nums: return 0
        # maxLength, count = 0, 0
        # for num in nums:
        #     if num == 0:
        #         maxLength = max(count, maxLength)
        #         count = 0
        #         continue
        #     count += 1
        # return max(count, maxLength)

        # 2滑动窗口
        left = right = maxLength = 0  # 指向开头位置 right负责向前移动 left负责记录开关位置
        while right < len(nums):
            if nums[right] == 0:
                maxLength = max(right - left, maxLength)
                right += 1  # 遇到0把移动left指针
                left = right
                continue
            right += 1
        return max(right - left, maxLength)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxConsecutiveOnes([1]))
