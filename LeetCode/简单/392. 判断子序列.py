class Solution(object):
    def isSubsequence(self, s, t):
        """
        https://leetcode-cn.com/problems/is-subsequence/
        :type s: str
        :type t: str
        :rtype: bool
        thinking:二分查找
        """
        if len(s) > len(t): return False

        inSet = {}
        for i, letter in enumerate(t):
            if letter not in inSet:
                inSet[letter] = [i]
            else:
                inSet[letter].append(i)

        last_index = -1
        for letter in s:
            if letter not in inSet:
                return False  # 如果s不包含直接返回
            left, indexes = 0, inSet[letter]
            right = len(indexes)
            while left < right:
                mid = left + (right - left) // 2
                if indexes[mid] > last_index:
                    right = mid
                else:
                    left = mid + 1
            if left == len(indexes):
                return False
            last_index = indexes[left]

        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isSubsequence('abc', 'accbcc'))
