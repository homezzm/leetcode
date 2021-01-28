class Solution(object):
    def combinationSum(self, candidates, target):
        """
        https://leetcode-cn.com/problems/combination-sum/
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        给定一个无重复元素的数组candidates和一个目标数target，
        找出candidates中所有可以使数字和为target的组合。
        candidates中的数字可以无限制重复被选取。
        说明：所有数字（包括 target）都是正整数。解集不能包含重复的组合。
        输入：candidates = [2,3,6,7], target = 7,
        所求解集为：[[7],[2,2,3]]
        https://leetcode-cn.com/problems/combination-sum/solution/gua-he-xin-shou-peng-you-de-shi-pin-jiang-jie-ru-h/
        这个题解，解答了startIndex的疑惑
        """

        res = []
        if not candidates or target <= 0: return res
        candidates = sorted(candidates)

        def backtrack(sumVal, startIndex, paths):
            if sumVal == target:
                res.append(paths[:])
                return

            for i in range(startIndex, len(candidates)):
                # 一个剪枝的动作，先把列表排好序，然后提前判断下，结果是否已经大于目标值
                val = sumVal + (candidates[i])
                if val > target: break
                paths.append(candidates[i])
                backtrack(val, i, paths)
                paths.pop()

        backtrack(0, 0, [])
        return res

        # def backtrack(startIndex, paths):
        #     sumVal = sum(paths)
        #     if sumVal == target:
        #         res.append(paths[:])
        #         return
        #     elif sumVal > target:
        #         return
        #
        #     for i in range(startIndex, len(candidates)):
        #         paths.append(candidates[i])
        #         backtrack(i, paths)
        #         paths.pop()
        #
        # backtrack(0, [])
        # return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum([2,7,6,3,5,1], 9))
