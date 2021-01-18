class Solution(object):
    def reverseString(self, s):
        """
        https://leetcode-cn.com/problems/reverse-string/
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        if not s: return s
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

if __name__ == '__main__':
    solution=Solution()
    li=["h","e","l","l","o"]
    solution.reverseString(li)
    print(li)

