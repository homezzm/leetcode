class Solution(object):
    def generateParenthesis(self, n):
        """
        https://leetcode-cn.com/problems/generate-parentheses/
        :type n: int
        :rtype: List[str]
        数字 n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
        示例 1：输入：n = 3    输出：["((()))","(()())","(())()","()(())","()()()"]
        示例 2：输入：n = 1   输出：["()"]
        """

        if n <= 0: return []
        res = []

        # open开括号的数量 #close闭括号的数量
        # 如果open大于n 或 close大于open就结束
        def dfs(paths, open, close):
            if open > n or close > open: return
            if len(paths) == 2 * n:
                res.append(paths)
                return
            dfs(paths + '(', open + 1, close)
            dfs(paths + ')', open, close + 1)

        dfs('', 0, 0)

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))
