class Solution(object):
    def arrangeCoins(self, n):
        """
        https://leetcode-cn.com/problems/arranging-coins/
        :type n: int
        :rtype: int
        thinking:
        1.规律 第一行1，第二行2，第三行3，第n行n
        2.每生成一行时都判断剩余的个数量否可以满足下一行，如果不可以直接返回
        """
        # count = 0
        # for i in range(1, n + 1):
        #     count += i
        #
        #     if n - count < i + 1:
        #         return i
        # return 0
        i = 1
        while i <= n:
            n -= i
            i += 1
        return i - 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.arrangeCoins(0))
