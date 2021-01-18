class Solution(object):
    def makeGood(self, s):
        """
        https://leetcode-cn.com/problems/make-the-string-great/
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 1: return s
        stack = []
        for i in range(len(s)):
            stack.append(s[i])

            if len(stack) < 2: continue

            if ord(stack[-1]) - ord(stack[-2]) == 32 or \
                    ord(stack[-2]) - ord(stack[-1]) == 32:
                stack.pop()
                stack.pop()

        return ''.join(stack)


if __name__ == '__main__':
    solution = Solution()
    print(solution.makeGood('s'))
