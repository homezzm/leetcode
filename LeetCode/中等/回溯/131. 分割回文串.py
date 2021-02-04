class Solution(object):
    def partition(self, s):
        """
        https://leetcode-cn.com/problems/palindrome-partitioning/
        :type s: str
        :rtype: List[List[str]]
        给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
        返回 s 所有可能的分割方案。
        输入: "aab"   输出:[["aa","b"],["a","a","b"]]
        """
        res = []
        if not s: return res

        def backtrack(lastStr, paths):
            if len(lastStr) == 0:  # 如果字符串没有了，就代表分割完了
                res.append(paths[:])
                return

            for i in range(len(lastStr)):
                upper = lastStr[:i + 1]  # a
                lower = lastStr[i + 1:]  # 剩余的字符串 ab

                if not self.isPalindrome(upper): continue

                paths.append(upper)
                backtrack(lower, paths)
                paths.pop()

        backtrack(s, [])
        return res

    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    # 第一种方式，不好理解
    # def partition(self, s):
    #     """
    #     https://leetcode-cn.com/problems/palindrome-partitioning/
    #     :type s: str
    #     :rtype: List[List[str]]
    #     给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
    #     返回 s 所有可能的分割方案。
    #     输入: "aab"   输出:[["aa","b"],["a","a","b"]]
    #     """
    #     res = []
    #     if not s: return res
    #
    #     def backtrack(startInx, paths):
    #         if startInx >= len(s):
    #             res.append(paths[:])
    #             return
    #
    #         for i in range(startInx, len(s)):
    #
    #             if not self.isPalindrome(s, startInx, i):
    #                 continue
    #
    #             paths.append(s[startInx:i + 1])
    #             backtrack(i + 1, paths)
    #             paths.pop()
    #
    #     backtrack(0, [])
    #     return res
    #
    # def isPalindrome(self, s, i, j):
    #     while i < j:
    #         if s[i] != s[j]:
    #             return False
    #         i += 1
    #         j -= 1
    #
    #     return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.partition('aab'))
