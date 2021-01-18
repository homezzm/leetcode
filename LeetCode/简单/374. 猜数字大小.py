# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
def guess(num):
    """
    -1：我选出的数字比你猜的数字小 pick < num
    1：我选出的数字比你猜的数字大 pick > num
    0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
    :param num:
    :return:
    """
    pass


class Solution(object):
    def guessNumber(self, n):
        """
        https://leetcode-cn.com/problems/guess-number-higher-or-lower/
        :type n: int
        :rtype: int
        """

        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            result = guess(mid)
            if result == 0:
                return mid
            if result == 1:  # pick > num
                left = mid + 1
            else:
                right = mid - 1

if __name__ == '__main__':
    solution=Solution()
    solution.guessNumber(10)