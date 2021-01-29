class Solution(object):
    def permutation(self, S):
        """
        https://leetcode-cn.com/problems/permutation-i-lcci/
        :type S: str
        :rtype: List[str]
        无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。
        示例1:输入：S = "qwe"   输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
        示例2:输入：S = "ab"    输出：["ab", "ba"]
        """

        if not S or len(S) <= 1: return []
        res, length = [], len(S)

        def backtrack(used, paths):
            if length == len(paths):
                res.append(''.join(paths))
                return

            for i in range(length):
                if used[i]: continue
                used[i] = True
                paths.append(S[i])
                backtrack(used, paths)
                used[i] = False
                paths.pop()

        backtrack([False] * length, [])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.permutation('qwe'))
