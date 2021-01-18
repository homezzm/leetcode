class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        https://leetcode-cn.com/problems/license-key-formatting/
        :type S: str
        :type K: int
        :rtype: str
        输入：S = "5F3Z-2e-9-w", K = 4     输出："5F3Z-2E9W"
        输入：S = "2-5g-3-J", K = 2    输出："2-5G-3J"
        thinking:
        1先去掉所有的“-”主s变成一个完整字符串
        然后用s的长度mod K，余数就是第一个串的长度，
        整除就是应该有几个k的长度
        """
        S = S.replace('-', '').upper()[::-1]
        res = ''
        for i in range(len(S)):
            if i % K == 0 and i != 0:
                res = '-' + res
            res = S[i] + res
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.licenseKeyFormatting("2-5g-3-J", 2))
