import string
class Solution(object):
    def letterCasePermutation(self, S):
        """
        https://leetcode-cn.com/problems/letter-case-permutation/
        :type S: str
        :rtype: List[str]
        给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。
        返回所有可能得到的字符串集合。
        输入：S = "a1b2"   输出：["a1b2", "a1B2", "A1b2", "A1B2"]
        输入：S = "3z4"    输出：["3z4", "3Z4"]
        输入：S = "12345"  输出：["12345"]
        """
        #这是题解中的思路，比较清奇
        if not S:
            return []
        res = ['']
        for i in S:
            temp = []
            for j in res:
                if i in string.ascii_letters:
                    temp.append(j + i.upper())
                    temp.append(j + i.lower())
                else:
                    temp.append(j + i)
            res = temp
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCasePermutation('z4'))

    # ["a1b2", "a1B2", "A1b2", "A1B2"]
    # ['a1b2', 'A1b2', 'A1B2']
    # print(solution.toUpper('A1b2'))
