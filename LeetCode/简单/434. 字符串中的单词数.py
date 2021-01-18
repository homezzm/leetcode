class Solution(object):
    def countSegments(self, s):
        """
        https://leetcode-cn.com/problems/number-of-segments-in-a-string/
        :type s: str
        :rtype: int
        thinking:
        1.去掉前后空格，判断是否为空，如空返回0
        2.使用内置函数根据空格进行分割转成列表统计数量即可
        """
        s = s.strip()
        if not s: return 0
        return len(list(s.split()))


if __name__ == '__main__':
    solution = Solution()
    print(solution.countSegments(' He   llo'))
