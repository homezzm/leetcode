class Solution(object):

    def calPoints(self, ops):
        """
        https://leetcode-cn.com/problems/baseball-game/
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))

        return sum(stack)


if __name__ == '__main__':
    solution = Solution()
    print(solution.calPoints(["5", "2", "C", "D", "+"]))
