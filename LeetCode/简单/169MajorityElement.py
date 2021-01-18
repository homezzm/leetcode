class Solution(object):
    def majorityElement(self, nums):
        """
        https://leetcode-cn.com/problems/majority-element/
        """
        candidate, count = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = nums[i]
                count = 1
        return candidate


if __name__ == '__main__':
    solution = Solution()
    print(solution.majorityElement( [2,2,1,1,1,2,2]))
