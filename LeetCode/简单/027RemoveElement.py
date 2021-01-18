class Solution:
    def removeElement(self, nums, val):
        # 双指针思路 i与j分别指向头与尾
        # 正向循环，当i找到与val相同的元素时，
        # 与j所在的的元素进行交换，交换后j指针向前移动，
        # 终止条件为ij指针重叠
        # 最后val的值应该都是列表的最后

        ans=0
        for num in nums:
            if num !=val:
                nums[ans]=num
                ans+=1
        return ans

        # n = len(nums)
        # if n <= 1 and val in nums:
        #     return 0
        # elif n <= 1:
        #     return n
        # right = n - 1
        # for left in range(0, n):
        #     if left >= right: break
        #     if nums[left] == val:
        #         if nums[left] == nums[right]:
        #             right -= 1
        #         nums[left], nums[right] = nums[right], nums[left]
        #         right -= 1
        # print(nums)
        # return right + 1


if __name__ == '__main__':
    solution = Solution()
    li = [2]
    print(solution.removeElement(li, 2))
