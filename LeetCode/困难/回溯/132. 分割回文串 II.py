class Solution(object):
    def minCut(self, s):
        """
        https://leetcode-cn.com/problems/palindrome-partitioning-ii/
        :type s: str
        :rtype: int
        给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。返回符合要求的最少分割次数。
        输入: "aab"   输出: 1
        解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
        其实就是求树的最小高度

        回溯算法超时啦！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        """
        if not s: return 0
        cut = float('inf')

        def backtrack(lastStr, step):
            if len(lastStr) == 0:
                nonlocal cut
                cut = min(cut, step)
                return

            for i in range(len(lastStr)):
                first = lastStr[:i + 1]  # a
                last = lastStr[i + 1:]  # ab
                if not self.isPalindrome(first): continue

                step += 1
                backtrack(last, step)
                step -= 1

        backtrack(s, 0)
        return cut - 1 #这地方！！！

    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCut('aab'))
