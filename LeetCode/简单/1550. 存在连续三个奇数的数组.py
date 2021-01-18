class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        https://leetcode-cn.com/problems/three-consecutive-odds/
        :type arr: List[int]
        :rtype: bool
        thinking:暴力：数组中每个元素mod2不为0，计数
        """
        if not arr: return False
        count = 0
        for i in arr:
            if i % 2 != 0:
                count += 1
            elif count >= 3:  # 已经有大于连续三个都是奇数的子数组了
                return True
            else:
                count = 0
        return count >= 3


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))
