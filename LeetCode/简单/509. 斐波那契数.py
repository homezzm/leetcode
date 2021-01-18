class Solution(object):
    def fib(self, n):
        """
        https://leetcode-cn.com/problems/fibonacci-number/
        :type n: int
        :rtype: int
        """
        f = [0, 1, 1]
        if n > 2:
            for i in range(n - 2):
                f.append(f[-1] + f[-2])
        return f[n]


if __name__ == '__main__':
    solution = Solution()
    print(solution.fib(5))
