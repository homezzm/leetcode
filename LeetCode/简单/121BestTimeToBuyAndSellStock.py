import sys


class Solution(object):
    def maxProfit(self, prices):
        """
        https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
        :type prices: List[int]
        :rtype: int
        """
        minProfit = sys.maxsize
        maxProfit = 0
        for price in prices:
            if price < minProfit:
                minProfit = price
            if price - minProfit > maxProfit:
                maxProfit = price - minProfit
        return maxProfit

if __name__ == '__main__':
    solution=Solution()
    print(solution.maxProfit( [7,1,5,3,6,4]))
