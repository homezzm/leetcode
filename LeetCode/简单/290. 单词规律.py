class Solution(object):
    def wordPattern(self, pattern, s):
        """
        https://leetcode-cn.com/problems/word-pattern/
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern_list = list(pattern)
        str_list = s.split()

        if len(str_list) != len(pattern_list) or len(set(str_list)) != len(set(pattern_list)):
            return False

        for i in range(len(str_list) - 1):
            p_first, p_second = pattern_list[i], pattern_list[i + 1]
            s_first, s_second = str_list[i], str_list[i + 1]

            if p_first == p_second and s_first != s_second:
                return False
            if p_first != p_second and s_first == s_second:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordPattern("abba", "dog cat cat fish"))
