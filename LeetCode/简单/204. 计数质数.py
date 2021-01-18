class Solution(object):
    def countPrimes(self, n):
        """
        https://leetcode-cn.com/problems/count-primes/
        :type n: int
        :rtype: int
        """
        if n < 2: return 0
        count = 0
        signs = [True] * n
        for i in range(2, n):
            if signs[i]:
                count += 1
                for j in range(i * i, n, i):
                    signs[j] = False
        return count

if __name__ == '__main__':
    solution = Solution()
    print(solution.countPrimes(10))
