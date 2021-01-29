class Solution(object):
    def countVowelStrings(self, n):
        """
        https://leetcode-cn.com/problems/count-sorted-vowel-strings/
        :type n: int
        :rtype: int
        给你一个整数 n，请返回长度为 n 、仅由元音 (a, e, i, o, u) 组成且按 字典序排列 的字符串数量。
        字符串 s 按 字典序排列 需要满足：对于所有有效的 i，s[i]
        在字母表中的位置总是与 s[i+1] 相同或在 s[i+1] 之前。
        输入：n = 2 输出：15
        解释：仅由元音组成的 15 个字典序字符串为
        ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]
        注意，"ea" 不是符合题意的字符串，因为 'e' 在字母表中的位置比 'a' 靠后
        """

        #回溯做的，效率非常差，到时候用动态规划做一次
        res = 0
        if n <= 0: return res
        li = ['a', 'e', 'i', 'o', 'u']

        def backtrack(startInx, paths):
            if len(paths) == n:
                nonlocal res
                res += 1
                return

            for i in range(startInx, len(li)):
                paths.append(li[i])
                backtrack(i, paths)
                paths.pop()

        backtrack(0, [])
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.countVowelStrings(2))
