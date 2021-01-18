class Solution(object):
    def isPowerOfFour(self, n):
        """
        https://leetcode-cn.com/problems/power-of-four/
        :type n: int
        :rtype: bool
        """
        if n < 1: return False
        while n % 4 == 0:
            n //= 4
        return n == 1
