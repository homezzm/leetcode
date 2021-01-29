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

        res, S, length = [], sorted(S), len(S)  # 排下序，使重复的都在一起

        def backtrack(used, paths):
            if length == len(paths):
                res.append(''.join(paths))
                return

            for i in range(length):
                if used[i]:
                    continue  # 已经选择过的不需要再放进去了
                if i > 0 and S[i] == S[i - 1] and not used[i - 1]:
                    continue  # 如果当前节点与他的前一个节点一样，并其他的前一个节点已经被遍历过了，那我们也就不需要了。

                used[i] = True
                paths.append(S[i])
                backtrack(used, paths)
                used[i] = False
                paths.pop()

        backtrack([False] * length, [])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.permutation('qqe'))
