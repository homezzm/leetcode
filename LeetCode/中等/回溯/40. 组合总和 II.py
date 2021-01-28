class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        https://leetcode-cn.com/problems/combination-sum-ii/
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
        candidates 中的每个数字在每个组合中只能使用一次。
        说明：所有数字（包括目标数）都是正整数。解集不能包含重复的组合。

        输入: candidates = [10,1,2,7,6,1,5], target = 8,
        所求解集为:[[1, 7],[1, 2, 5],[2, 6],[1, 1, 6]]
        """
        res = []
        if not candidates or target <= 0: return res

        def backtrack(sumVal, startInx, paths):
            if sumVal == target:
                paths = sorted(paths)
                if paths not in res:
                    res.append(paths[:])
                return

            for i in range(startInx, len(candidates)):
                val = sumVal + candidates[i]
                if val > target:  # 做个剪技
                    break
                if i > 0 and i > startInx and candidates[i] == candidates[i - 1]:
                    continue
                paths.append(candidates[i])
                backtrack(val, i + 1, paths)
                paths.pop()

        backtrack(0, 0, [])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum2([1,1,1,2,3,4,5,5,3,6,1],27))
