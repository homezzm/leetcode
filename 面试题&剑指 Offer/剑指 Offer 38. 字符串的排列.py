class Solution(object):
    def permutation(self, s):
        """
        https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/
        :type s: str
        :rtype: List[str]
        输入一个字符串，打印出该字符串中字符的所有排列。
        你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
        示例:输入：s = "abc"    输出：["abc","acb","bac","bca","cab","cba"]
        """

        if not s: return []
        res = []
        s = sorted(s)

        def backtrack(used, paths):
            if len(paths) == len(s):
                res.append(''.join(paths))
                return

            for i in range(len(s)):
                if used[i]: continue
                if i > 0 and s[i] == s[i - 1] and used[i - 1]: break
                used[i] = True
                paths.append(s[i])
                backtrack(used, paths)
                used[i] = False
                paths.pop()

        backtrack([False] * len(s), [])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.permutation('aab'))
