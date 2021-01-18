class Solution(object):
    def twoSum(self, numbers, target):
        """
        https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([5, 25, 75], 100))
