class Solution(object):
    def moveZeroes(self, nums):
        """
        https://leetcode-cn.com/problems/move-zeroes/
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                # 当前元素!=0，就把其交换到左边，等于0的交换到右边
                nums[j],nums[i] = nums[i],nums[j]
                j+=1


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(nums)
