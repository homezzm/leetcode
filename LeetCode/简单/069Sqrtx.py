class Solution(object):
    def mySqrt(self, x):
        """
        实现int sqrt(int x)函数。
        计算并返回x的平方根，其中x 是非负整数。
        由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

        示例 1:
        输入: 4
        输出: 2

        示例 2:
        输入: 8
        输出: 2
        说明: 8 的平方根是 2.82842...,
        由于返回类型是整数，小数部分将被舍去。
        用二分查找实现的，有意思
        """
        left, right, ans = 0, x, -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans


import math

if __name__ == '__main__':
    print(math.sqrt(4))
    solution = Solution()
    print(solution.mySqrt(4))
