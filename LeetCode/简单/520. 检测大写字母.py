from collections import Counter


class Solution(object):
    def detectCapitalUse(self, word):
        """
        https://leetcode-cn.com/problems/detect-capital/
        :type word: str
        :rtype: bool
        thinking:
        1.暴力
        大写值为1
        小写值为0
        """

        if not word: return False
        uc = 0
        for i in range(len(word)):
            if word[i].isupper():
                uc += 1
                if uc <= i:
                    return False
        return uc == len(word) or uc <= 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.detectCapitalUse('Af'))
