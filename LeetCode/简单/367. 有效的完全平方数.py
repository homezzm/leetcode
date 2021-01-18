class Solution(object):
    def isPerfectSquare(self, num):
        """
        https://leetcode-cn.com/problems/valid-perfect-square/submissions/
        :type num: int
        :rtype: bool
        抄的
        4=1+3 9=1+3+5 16=1+3+5+7以此类推，模仿它可以使用一个while循环，
        不断减去一个从1开始不断增大的奇数，若最终减成了0，说明是完全平方数，否则，不是。
        """

        num1 = 1
        while num > 0:
            num -= num1
            num1 += 2
        return num == 0
