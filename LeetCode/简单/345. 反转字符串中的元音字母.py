class Solution(object):
    def reverseVowels(self, s):
        """
        https://leetcode-cn.com/problems/reverse-vowels-of-a-string/
        :type s: str
        :rtype: str
        """
        if not s: return s
        new_s_li = list(s)
        vowels = {'a','A', 'e','E', 'i','I', 'o','O', 'u','U'}
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1
            if s[left] in vowels and s[right] in vowels:
                new_s_li[left], new_s_li[right] = new_s_li[right], new_s_li[left]
                left += 1
                right -= 1
        return ''.join(new_s_li)

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseVowels("aA"))
