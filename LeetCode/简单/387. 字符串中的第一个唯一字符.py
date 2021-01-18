import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        https://leetcode-cn.com/problems/first-unique-character-in-a-string/
        :type s: str
        :rtype: int
        """
        if not s: return -1
        dicts = {c: s.count(c) for c in set(s)}  # collections.Counter(s)
        for key, val in dicts.items():
            if val == 1:
                return s.index(key)
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.firstUniqChar('aabbccddq'))
