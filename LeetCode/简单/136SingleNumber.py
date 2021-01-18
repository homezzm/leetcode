class Solution(object):
    """
    https://leetcode-cn.com/problems/single-number/
    """
    def singleNumber(self, nums):
        num = 0
        for i in nums:
            num ^= i
        return num


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([0, 1, 2, 1, 2]))
