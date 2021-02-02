class Solution(object):
    def countArrangement(self, n):
        """
        https://leetcode-cn.com/problems/beautiful-arrangement/
        :type n: int
        :rtype: int
        假设有从 1 到 N 的N个整数，如果从这N个数字中成功构造出一个数组，
        使得数组的第 i位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：
        第i位的数字能被i整除
        i 能被第 i 位上的数字整除
        现在给定一个整数 N，请问可以构造多少个优美的排列？
        输入: 2   输出: 2
        第 1 个优美的排列是 [1, 2]:
          第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
          第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除

        第 2 个优美的排列是 [2, 1]:
          第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
          第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
        """
        count = 0
        if n <= 0: return count

        def backtrack(used, inx):
            if inx > n:
                nonlocal count
                count += 1
                return

            for i in range(1, n + 1):
                if used[i - 1]: continue  # 如果当前数已经使用过
                if i % inx != 0 and inx % i != 0: continue  # 剪枝条件：如果不能被i或整除i
                used[i - 1] = True
                backtrack(used, inx + 1)
                used[i - 1] = False

        backtrack([False] * n, 1)
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.countArrangement(8))
