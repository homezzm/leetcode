class Solution(object):
    def backspaceCompare(self, S, T):
        """
        https://leetcode-cn.com/problems/backspace-string-compare/
        :type S: str
        :type T: str
        :rtype: bool
        """
        def build(strs):
            res = []
            for ch in strs:
                if ch != '#':
                    res.append(ch)
                elif res:
                    res.pop()
            return ''.join(res)
        return build(S)==build(T)


if __name__ == '__main__':
    solution = Solution()
    print(solution.backspaceCompare('ab##', 'c#d#'))
