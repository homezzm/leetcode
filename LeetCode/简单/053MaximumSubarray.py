class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        for i in range(1,n):
            if nums[i-1]>0:
                nums[i]+=nums[i-1]
        return max(nums)

if __name__ == '__main__':
    solution=Solution()
    print(solution.maxSubArray([-2]))