class Solution(object):
    def isAnagram(self, s, t):
        """
        https://leetcode-cn.com/problems/valid-anagram/
        :type s: str
        :type t: str
        :rtype: bool
        """
        slen, tlen = len(s), len(t)
        if slen != tlen: return False
        alpha = [0] * 26
        for i in range(slen):
            alpha[ord(s[i]) - ord('a')] += 1
            alpha[ord(t[i]) - ord('a')] -= 1
        for i in alpha:
            if i > 0:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))
