class Solution(object):
    def combinationSum3(self, k, n):
        """
        https://leetcode-cn.com/problems/combination-sum-iii/
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
        说明：所有数字都是正整数。解集不能包含重复的组合
        示例：输入: k = 3, n = 7     输出: [[1,2,4]]
             输入: k = 3, n = 9    输出: [[1,2,6], [1,3,5], [2,3,4]]
        """
        res, paths = [], []

        def backtracking(startIndex):
            if len(paths) == k:  # 已经够数了
                if sum(paths) == n:
                    res.append(paths[:])  # 收集组合中和等于n的路径
                return
            # for i in range(startIndex, 10): #剪枝
            for i in range(startIndex, 10 - (k - len(paths)) + 1):
                paths.append(i)
                backtracking(i + 1)
                paths.pop()

        backtracking(1)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum3(3, 9))
