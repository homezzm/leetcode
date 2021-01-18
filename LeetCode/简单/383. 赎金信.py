import collections


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        https://leetcode-cn.com/problems/ransom-note/
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(magazine) < len(ransomNote): return False
        # dicts = {}
        # for letter in magazine:
        #     if letter in dicts:
        #         dicts[letter] += 1
        #     else:
        #         dicts[letter] = 1
        dicts = collections.Counter(magazine)  # python自带的计数器
        for ransom in ransomNote:
            if ransom in dicts and dicts[ransom] > 0:
                dicts[ransom] -= 1
                continue
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.canConstruct("aa", "bb"))

