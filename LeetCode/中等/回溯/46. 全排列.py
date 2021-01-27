class Solution(object):
    def permute(self, nums):
        """
        https://leetcode-cn.com/problems/permutations/
        :type nums: List[int]
        :rtype: List[List[int]]
        给定一个 没有重复 数字的序列，返回其所有可能的全排列。
        输入: [1,2,3]
        输出:
        [
          [1,2,3],
          [1,3,2],
          [2,1,3],
          [2,3,1],
          [3,1,2],
          [3,2,1]
        ]
        """

        res = []

        def backtrack(paths):
            if len(paths) == len(nums):  # 够数了，收集起来
                res.append(paths[:])
                return  # 都够数了收集完这波就完事了

            # 开始多叉树的遍历
            for num in nums:  # 在选择列表中做选择
                if num in paths:  # 已经添加的就不要再填加了，因为题目要求是没有重复的序列
                    continue
                paths.append(num)  # 做选择
                backtrack(paths)
                paths.pop()  # 撤销选择

        backtrack([])
        return res
