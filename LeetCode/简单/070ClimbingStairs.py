class Solution(object):
    def climbStairs(self, n):
        f = [0, 1, 2]
        if n > 2:
            for i in range(n - 2):
                num = f[-1] + f[-2]
                f.append(num)
        return f[n]
