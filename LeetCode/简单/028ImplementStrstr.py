class Solution(object):
    def strStr(self, haystack, needle):
        """
        实现strStr()函数。
        给定一个haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回 -1。

        示例 1:
        输入: haystack = "hello", needle = "ll"
        输出: 2

        示例 2:
        输入: haystack = "aaaaa", needle = "bba"
        输出: -1
        说明:
        当needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
        对于本题而言，当needle是空字符串时我们应当返回 0 。这与C语言的strstr()以及 Java的indexOf()定义相符。
        """
        if not needle: return 0
        l, n = len(haystack), len(needle)
        if l < n: return -1
        for start in range(l - n + 1):
            if haystack[start:start + n] == needle:
                return start
        else:
            return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr('hello', 'll'))
