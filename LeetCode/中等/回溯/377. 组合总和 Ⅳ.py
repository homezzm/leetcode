class Solution(object):
    def combinationSum4(self, nums, target):
        """
        https://leetcode-cn.com/problems/combination-sum-iv/
        :type nums: List[int]
        :type target: int
        :rtype: int
        给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。
        nums = [1, 2, 3]    target = 4
        所有可能的组合为：
        (1, 1, 1, 1)
        (1, 1, 2)
        (1, 2, 1)
        (1, 3)
        (2, 1, 1)
        (2, 2)
        (3, 1)
        请注意，顺序不同的序列被视作不同的组合。因此输出为 7。
        """
        count = 0
        if not nums or target <= 0: return count
        nums = sorted(nums)

        def backtrack(sumVal, paths):
            if sumVal == target:
                nonlocal count
                count += 1
                return
            if sumVal > target: return

            for i in range(len(nums)):
                val = sumVal + nums[i]
                if val > target: break

                paths.append(nums[i])
                backtrack(val, paths)
                paths.pop()

        backtrack(0, [])
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum4([4,2,1], 24))
