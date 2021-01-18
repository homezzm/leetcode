class Solution(object):
    def rotate(self, nums, k):
        """
        https://leetcode-cn.com/problems/rotate-array/
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums: return nums

        n = len(nums)
        k %= n
        for _ in range(k):
            nums.insert(0, nums.pop())


if __name__ == '__main__':
    solution = Solution()
    nums=[1,2,3,4,5,6,7]
    solution.rotate(nums, 3)
    print(nums)
