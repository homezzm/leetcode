class Solution(object):
    def bitSquareSum(self, n):
        sum_num = 0
        while n > 0:
            bit = n % 10
            sum_num += bit * bit
            n //= 10
        return sum_num

    def isHappy(self, n):
        """
        https://leetcode-cn.com/problems/happy-number/
        """
        slow, fast = n, self.bitSquareSum(n)
        while slow != fast:
            slow = self.bitSquareSum(slow)
            fast = self.bitSquareSum(fast)
            fast = self.bitSquareSum(fast)
        return slow == 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(19))
