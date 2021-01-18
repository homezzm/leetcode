class Solution(object):
    def findComplement(self, num):
        """
        https://leetcode-cn.com/problems/number-complement/
        :type num: int
        :rtype: int
        thinking
        """
        res, num = '', bin(num)[2:]
        for i in num:
           res += '1' if i == '0' else '0'
        return int(res, 2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findComplement(0))
