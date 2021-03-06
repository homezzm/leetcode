class Solution(object):
    def letterCombinations(self, digits):
        """
        https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
        :type digits: str
        :rtype: List[str]
        给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
        给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
        输入："23"
        输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
        说明:尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
        """
        digitsLenght = len(digits)
        if digitsLenght == 0: return []

        phoneDicts = {0: "", 1: "", 2: "abc", 3: "def",
                      4: "ghi", 5: "jkl", 6: "mno",
                      7: "pqrs", 8: "tuv", 9: "wxyz"}

        res = []

        def backtrack(inx, paths):
            if digitsLenght == len(paths):
                res.append(''.join(paths))
                return

            digit = digits[inx] #找到第一个数字
            letters = phoneDicts[int(digit)]#根据数字找到对应字母
            for i in range(len(letters)):
                paths.append(letters[i])
                backtrack(inx+1,paths)
                paths.pop()

        backtrack(0,[])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations('23'))
