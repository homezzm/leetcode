class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/
        :type nums: List[int]
        :rtype: List[int]
        """
        # nums_set = set(nums)
        # li = []
        # for i in range(1, len(nums) + 1):
        #     if i not in nums_set:
        #         li.append(i)
        # return li

        for num in nums:
            index = abs(num) - 1
            # 始终保持nums[index]为负数
            nums[index] = -abs(nums[index])
        return [i + 1 for i, num in enumerate(nums) if num > 0]



if __name__ == '__main__':
    solution = Solution()
    print(solution.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])) 
