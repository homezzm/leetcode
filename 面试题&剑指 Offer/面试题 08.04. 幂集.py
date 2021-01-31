class Solution(object):
    def subsets(self, nums):
        """
        https://leetcode-cn.com/problems/power-set-lcci/
        :type nums: List[int]
        :rtype: List[List[int]]
        幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。
        说明：解集不能包含重复的子集。
        输入： nums = [1,2,3]
        输出：[[3],[1],[2],[1,2,3],[1,3],[2,3],[1,2],[]]
        """

        res = []
        if not nums: return res

        def backtrack(startInx, paths):
            res.append(paths[:])

            for i in range(startInx, len(nums)):
                paths.append(nums[i])
                backtrack(i + 1, paths)
                paths.pop()

        backtrack(0, [])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2]))