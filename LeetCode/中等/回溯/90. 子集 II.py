class Solution(object):
    def subsetsWithDup(self, nums):
        """
        https://leetcode-cn.com/problems/subsets-ii/
        :type nums: List[int]
        :rtype: List[List[int]]
        给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
        说明：解集不能包含重复的子集。
        thinking:有重复的就看下是否和上一个数相同，相同跳过即可，要先排下序
        输入: [1,2,2]
        输出:[ [2], [1], [1,2,2], [2,2], [1,2], []]
        """
        res = []
        if not nums: return res
        nums = sorted(nums)

        def backtrack(start, tracks):
            res.append(tracks[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]: #回溯的时候看是否和上一个元素相同
                    continue
                tracks.append(nums[i])
                backtrack(i + 1, tracks)
                tracks.pop()

        backtrack(0, [])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsetsWithDup([1,2,2]))
