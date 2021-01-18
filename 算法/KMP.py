class KMP:
    def getNext(self, next, s):
        j, next[0] = 0, 0
        for i in range(1, len(next)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]

            if s[i] == s[j]:
                j += 1

            next[i] = j


    def strStr(self, haystack, needle):
        if not needle: return -1

        needle_len = len(needle)
        next = [0] * needle_len
        self.getNext(next, needle)
        j = 0
        for i in range(len(haystack)):  # 其实这个对比过程与获取前缀表一样
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]

            if haystack[i] == needle[j]:
                j += 1

            if j == needle_len:
                return i - needle_len + 1  # 返回第一个找到的下标
        return -1


if __name__ == '__main__':
    kmp = KMP()
    print(kmp.strStr('aabaabaaf', 'aabaaf'))
    # 返回3，即从下标为3的位置开始有匹配的