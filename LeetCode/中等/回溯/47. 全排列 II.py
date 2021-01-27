class Solution(object):
    def permuteUnique(self, nums):
        """
        https://leetcode-cn.com/problems/permutations-ii/
        :type nums: List[int]
        :rtype: List[List[int]]
        给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
        输入：nums = [1,1,2] 像这种情况，可以把数组的索引添加到paths里，最后收集结果的时候在转成具体的值，
        因为这个数组内容有重复，但索引没有重复。
        输出：[[1,1,2], [1,2,1],[2,1,1]]
        输入：nums = [1,2,3]
        输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        """
        res = []
        nums = sorted(nums)  # 排下序让相同的元素在一起

        def backtrack(paths, used):
            if len(paths) == len(nums):
                res.append(paths[:])
                return

            for i in range(len(nums)):  # 数组的索引添加到paths里，最后收集结果的时候在转成具体的值
                if used[i]: continue  # 已经选择过的不需要再放进去了
                # 如果当前节点与他的前一个节点一样，并其他的前一个节点已经被遍历过了，那我们也就不需要了。
                if i > 0 and nums[i] == nums[i - 1] and used[i - 1]:
                    break

                used[i] = True
                paths.append(nums[i])
                backtrack(paths,used)
                used[i] = False
                paths.pop()

        backtrack([], [False] * len(nums))
        return res

        # 以下代码没有好做的剪枝操作
        # res = []
        #
        # def backtrack(paths):
        #     if len(paths) == len(nums):
        #         pathsRes = [nums[inx] for inx in paths]
        #         if pathsRes not in res:
        #             res.append(pathsRes)
        #         return
        #
        #     for i in range(len(nums)): #数组的索引添加到paths里，最后收集结果的时候在转成具体的值
        #         if i in paths: continue
        #         paths.append(i)
        #         backtrack(paths)
        #         paths.pop()
        #
        # backtrack([])
        # return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.permuteUnique([1, 1, 2]))

    # li=[[1, 1, 2], [1, 2, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 1, 1]]
    # ss = [1,1,2]
    # print(ss not in li)
