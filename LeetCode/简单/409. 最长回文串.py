from collections import Counter


class Solution(object):
    def longestPalindrome(self, s):
        """
        https://leetcode-cn.com/problems/longest-palindrome/
        :type s: str
        :rtype: int
        abccccdd
        dccaccd
        dccbccd
        thinking:构造一个字典，k=字母 v=这个字母在s中出现的次数
        只要是偶数就是回文，把所有偶数//2计数后，如果还有剩余的奇数就整体长度在加1即可
        因为题目要求的是最长的
        """
        if not s: return 0
        if len(s) == 1: return 1

        count, dicts = 0, Counter(s)
        for v in dicts.values():
            count += v // 2 * 2  # [v=2 2//2*2=2] [v=3 3//2*2=2]
            if count % 2 == 0 and v % 2 == 1:  # 有一个是奇数的，结果加1
                count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome("abccccdd"))
