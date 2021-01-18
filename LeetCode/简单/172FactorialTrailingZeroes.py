class Solution(object):
    def trailingZeroes(self, n):
        count = 0
        while n > 0:
            count += n // 5
            n = n // 5
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.trailingZeroes(10))
