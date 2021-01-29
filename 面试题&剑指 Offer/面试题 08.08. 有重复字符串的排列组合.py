class Solution(object):
    def permutation(self, S):
        """
        https://leetcode-cn.com/problems/permutation-ii-lcci/
        :type S: str
        :rtype: List[str]
        有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。
        示例1:输入：S = "qqe"    输出：["eqq","qeq","qqe"]
        """

        if not S or len(S) <= 1: return []

        res = []

        def backtrack(startInx, paths):
            if len(S) == len(paths):
                res.append(''.join(paths))
                return

            for i in range(startInx, len(S)):
                # 剪下支，把重复的去掉
                if i > 0 and i > startInx and S[i] == S[i - 1]:
                    continue

                paths.append(S[i])
                backtrack(startInx + 1, paths)
                paths.pop()

        backtrack(0, [])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.permutation('qqe'))
