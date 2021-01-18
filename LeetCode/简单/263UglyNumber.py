class Solution(object):
    def isUgly(self, num):
        """
        https://leetcode-cn.com/problems/ugly-number/
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        while num != 1:
            if num % 2 == 0:
                num //= 2
                continue
            elif num % 3 == 0:
                num //= 3
                continue
            elif num % 5 == 0:
                num //= 5
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isUgly(14))
