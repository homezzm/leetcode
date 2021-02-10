class Solution(object):
    def generateParenthesis(self, n):
        """
        https://leetcode-cn.com/problems/bracket-lcci/
        :type n: int
        :rtype: List[str]
        括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。
        说明：解集不能包含重复的子集。
        """

        if n <= 0: return []
        res = []

        def dfs(paths, left, right):
            if left > n or right > left : return
            if len(paths) == n * 2:  # 因为括号都是成对出现的
                res.append(paths)
                return

            dfs(paths + '(', left + 1, right)  # 生成一个就加一个
            dfs(paths + ')', left, right + 1)

        dfs('', 0, 0)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))
