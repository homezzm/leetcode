from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        https://leetcode-cn.com/problems/find-the-difference/
        :type s: str
        :type t: str
        :rtype: str
        两字符串转列表合并后进行异或
        时间复杂度O(n) 空间复杂度O(n)
        """
        li = list(s)
        li.extend(list(t))
        val = 0
        for i in li:
            val ^= ord(i)
        return chr(val)


if __name__ == '__main__':
    solution = Solution()
    print(solution.findTheDifference('ae', 'aea'))
