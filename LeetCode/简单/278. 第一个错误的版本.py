# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    return True if version == 1 else False


class Solution:
    def firstBadVersion(self, n):
        """
        https://leetcode-cn.com/problems/first-bad-version/
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    solution = Solution()
    print(solution.firstBadVersion(4))
